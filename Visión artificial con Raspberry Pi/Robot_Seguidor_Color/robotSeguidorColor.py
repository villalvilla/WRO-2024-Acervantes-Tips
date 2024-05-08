from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
import RPi.GPIO as gpio
import numpy as np

def extractColor(frame, r):
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imagenNueva = frameHSV[r[1]:r[1]+r[3],r[0]:r[0]+r[2]]
    H,S,V = imagenNueva[:,:,0], imagenNueva[:,:,1], imagenNueva[:,:,2]
    hMin, hMax = np.min(H), np.max(H)
    sMin, sMax = np.min(S), np.max(S)
    vMin, vMax = np.min(V), np.max(V)

    bajo = np.array([hMin, sMin, vMin], np.uint8)
    alto = np.array([hMax, sMax, vMax], np.uint8)
    return bajo, alto


def testColor(frame, bajo, alto):
    frame2 = frame.copy()
    frameHSV = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, bajo, alto)
    cx, cy, area = obtenerCentroide(mask)
    frame2[mask == 255] = (0,255,0)
    cv2.circle(frame2, (cx,cy), 5,(0,0,255), -1)
    return frame2, mask, cx,cy, area


def obtenerCentroide(imgBin):
    cx = 0
    cy = 0
    cBlancas = cv2.findNonZero(imgBin)

    try:
        area = np.sum(imgBin == 255)
        sumX, sumY = np.sum(cBlancas, axis=0).squeeze()
        nPuntos = len(cBlancas)
        cx = int(sumX / nPuntos)
        cy = int(sumY / nPuntos)
    except:
        pass

    return cx, cy, area


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

    elif comando == "r":
        MA1.ChangeDutyCycle(cTrabajo)
        MA2.ChangeDutyCycle(0)
        MB1.ChangeDutyCycle(cTrabajo)
        MB2.ChangeDutyCycle(0)

    elif comando == "f":
        MA1.ChangeDutyCycle(0)
        MA2.ChangeDutyCycle(cTrabajo)
        MB1.ChangeDutyCycle(0)
        MB2.ChangeDutyCycle(cTrabajo)

    elif comando == "o":
        MA1.ChangeDutyCycle(0)
        MA2.ChangeDutyCycle(0)
        MB1.ChangeDutyCycle(0)
        MB2.ChangeDutyCycle(0)

p1MA = 12
p2MA = 32
p1MB = 33
p2MB = 35

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


cuenta = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    try:
        if cuenta == 10:
            roi = cv2.selectROI("frame", image, fromCenter=False, showCrosshair=True)
            roi = tuple(map(int,roi))
            bajo, alto = extractColor(image, roi)
        elif cuenta > 10:
            image, mask, cx, cy, area = testColor(image, bajo, alto)

            if cx >= lim1X:
                accion = "d"
            elif cx <= lim2X:
                accion = "i"
            elif area <= 15000: accion = "f" elif area >= 40000:
                accion = "r"
            else:
                accion = "o"
                
            print(area, accion)
                
            if accionOld == accion and cicloTrabajo < 26: cicloTrabajo += 2 elif cicloTrabajo > 26:
                cicloTrabajo = 26
                
            elif accionOld != accion:
                cicloTrabajo = 0
                
            mover(accion, cicloTrabajo)
            accionOld = accion
    except:
        mover("o", 0)

    cv2.imshow("frame", image)
    rawCapture.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        mover("o", 0)
        gpio.cleanup()
        break
    cuenta += 1
cv2.destroyAllWindows()
