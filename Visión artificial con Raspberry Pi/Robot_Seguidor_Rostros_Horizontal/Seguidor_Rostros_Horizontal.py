# Importamos las librerías, exactamente igual que en los ejemplos de la semana pasada:
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import RPi.GPIO as gpio

# Definimos los pines donde vamos a conectar los motores. 
# ¡OJO! Estamos usando el driver de motor L298N:
# ¡OJO (2)! Es posible dejar los ENA y ENB del driver L298N con su jumper original y regular la velocidad directamente con señales PWM en cada pin (alante/atrás). Recordad el driver no es más que un puente H, que deja pasar la corriente del colector al emisor de cada transistor en un sentido u otro. En este caso estamos usando ese sistema, para ahorrar líneas de código:
p1MA = 12
p2MA = 32
p1MB = 33
p2MB = 35

# Definimos las variables de control, tamaño del Frame y Sensibilidad:
resolucion = (640,480)
sensibilidad = 20
accion = ""
accionOld = "o"
cicloTrabajo = 0     # % de Velocidad de cada PIN del Driver de Motor
frecuencia = 1000    # Frecuencia de Trabajo de los pines PWM

# Definimos los límites de trabajo entre los que va a trabajar en "Centroide" que calcule:
lim1X = int(resolucion[0]/2) + sensibilidad
lim2X = int(resolucion[0]/2) - sensibilidad

# Inicializo las GPIO de la RPi:
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

# Configuro los pines de los motores como pines de salida en las GPIO:
gpio.setup(p1MA, gpio.OUT)
gpio.setup(p2MA, gpio.OUT)
gpio.setup(p1MB, gpio.OUT)
gpio.setup(p2MB, gpio.OUT)

# Como ya os expliqué más arriba, uso los pines del driver de motor como PWM, de tal modo que si pongo ambos pines de un motor a CERO, se para, mientras que si
# pongo % de voltaje en uno de los pines va hacia delante, y si pongo % de voltaje en el otro va hacia atrás:
MA1 = gpio.PWM(p1MA, frecuencia)
MA2 = gpio.PWM(p2MA, frecuencia)
MB1 = gpio.PWM(p1MB, frecuencia)
MB2 = gpio.PWM(p2MB, frecuencia)

MA1.start(cicloTrabajo)
MA2.start(cicloTrabajo)
MB1.start(cicloTrabajo)
MB2.start(cicloTrabajo)

# Inicializo la Cámara:
camera = PiCamera()
camera.resolution = resolucion
rawCapture = PiRGBArray(camera, size=resolucion)
time.sleep(0.3)

# Inicializo el modelo de Red Neuronal con Haar Cascade:
fCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# Función principal del driver de motor. Según nos manden muévete con X velocidad (cTrabajo) a la izquierda (i), derecha (d) o parado (o):
# ¡Ojo! Esta función puede funcionar como stub para los que uséis los motores 360º, por lo que sólo deberéis cambiar según reciba (i, d, o) el código específico para los servos 360:
def mover(comando, cTrabajo):
    if comando == "i":
        MA1.ChangeDutyCycle(0)
        MA2.ChangeDutyCycle(cTrabajo)
        MB1.ChangeDutyCycle(cTrabajo)
        MB2.ChangeDutyCycle(0)
        
    elif comando == "d":
        MA1.ChangeDutyCycle(cTrabajo)
        MA2.ChangeDutyCycle(0)
        MB1.ChangeDutyCycle(0)
        MB2.ChangeDutyCycle(cTrabajo)
        
    elif comando == "o":
        MA1.ChangeDutyCycle(0)
        MA2.ChangeDutyCycle(0)
        MB1.ChangeDutyCycle(0)
        MB2.ChangeDutyCycle(0)

# Bucle principal de movimiento del robot, según detecte cara o no. 
#¡OJO! Tened en cuenta que estamos usando sólo movimiento horizontal. Os recomiendo poner un móvil con una cara delante de la Cámara para mover Izquierda/Derecha.
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = fCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(100,100))
    try:
        (x,y,w,h) = faces[0]
        cv2.rectangle(image, (x,y), (x+w, y+w), (0,255,0), 2)
        cx = (x + int(w/2))
        cy = (y + int(h/2))
        image = cv2.circle(image, (cx,cy), 5, (0,0,255), -1)
        
        if cx >= lim1X:
            accion = "d"
        elif cx <= lim2X:
            accion = "i"
        else:
            accion = "o"
            
        if accionOld == accion and cicloTrabajo < 26: 
            cicloTrabajo += 2 
        elif cicloTrabajo > 26:
            cicloTrabajo = 26
        elif accionOld != accion:
            cicloTrabajo = 0
            
        mover(accion, cicloTrabajo)
        accionOld = accion
    except:
        mover("o", 0)
        
    
    cv2.imshow("Frame", image)
    rawCapture.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        mover("o", 0)
        gpio.cleanup()
        break
cv2.destroyAllWindows()
