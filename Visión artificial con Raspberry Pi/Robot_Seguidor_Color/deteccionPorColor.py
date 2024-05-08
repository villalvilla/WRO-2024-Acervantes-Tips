from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2
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
    cx, cy = obtenerCentroide(mask)
    frame2[mask == 255] = (0,255,0)
    cv2.circle(frame2, (cx,cy), 5,(0,0,255), -1)
    return frame2, mask, cx,cy


def obtenerCentroide(imgBin):
    cx = 0
    cy = 0
    cBlancas = cv2.findNonZero(imgBin)
    
    try:
        sumX, sumY = np.sum(cBlancas, axis=0).squeeze()
        nPuntos = len(cBlancas)
        cx = int(sumX / nPuntos)
        cy = int(sumY / nPuntos)
    except:
        pass
    
    return cx, cy

resolucion = (640,480)

camera = PiCamera()
camera.resolution = resolucion
rawCapture = PiRGBArray(camera, size=resolucion)
time.sleep(0.3)

cuenta = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    if cuenta == 10:
        roi = cv2.selectROI("frame", image, fromCenter=False, showCrosshair=True)
        roi = tuple(map(int,roi))
        bajo, alto = extractColor(image, roi)
    elif cuenta > 10:
        f, mask, cx, cy = testColor(image, bajo, alto)
        print(cx,cy)
        cv2.imshow("frame", f)
        cv2.imshow("frame2", mask)
        
    rawCapture.truncate(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cuenta += 1
