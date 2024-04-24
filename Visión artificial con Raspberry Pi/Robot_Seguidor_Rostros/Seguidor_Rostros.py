# Importamos las librerías, exactamente igual que en los ejemplos de la semana pasada:
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import RPi.GPIO as gpio

# Definimos los pines donde vamos a conectar los motores. ¡OJO! Estamos usando el driver de motor L298N:
p1MA = 12
p2MA = 32
p1MB = 33
p2MB = 35

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

resolucion = (640,480)
sensibilidad = 20
accion = ""
accionOld = "o"
cicloTrabajo = 0
frecuencia = 1000

lim1X = int(resolucion[0]/2) + sensibilidad
lim2X = int(resolucion[0]/2) - sensibilidad

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

gpio.setup(p1MA, gpio.OUT)
gpio.setup(p2MA, gpio.OUT)
gpio.setup(p1MB, gpio.OUT)
gpio.setup(p2MB, gpio.OUT)

MA1 = gpio.PWM(p1MA, frecuencia)
MA2 = gpio.PWM(p2MA, frecuencia)
MB1 = gpio.PWM(p1MB, frecuencia)
MB2 = gpio.PWM(p2MB, frecuencia)

MA1.start(cicloTrabajo)
MA2.start(cicloTrabajo)
MB1.start(cicloTrabajo)
MB2.start(cicloTrabajo)

camera = PiCamera()
camera.resolution = resolucion
rawCapture = PiRGBArray(camera, size=resolucion)
time.sleep(0.3)

fCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

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
        
        if cx &gt;= lim1X:
            accion = "d"
        elif cx &lt;= lim2X:
            accion = "i"
        else:
            accion = "o"
            
        if accionOld == accion and cicloTrabajo &lt;26: 
            cicloTrabajo += 2 
        elif cicloTrabajo &gt; 26:
            cicloTrabajo = 26
        elif accionOld != accion:
            cicloTrabajo = 0
            
        mover(accion, cicloTrabajo)
        accionOld = accion
    except:
        mover("o", 0)
        
    
    cv2.imshow("Frame", image)
    rawCapture.truncate(0)
    key = cv2.waitKey(1) &amp; 0xFF
    if key == ord("q"):
        mover("o", 0)
        gpio.cleanup()
        break
cv2.destroyAllWindows()
