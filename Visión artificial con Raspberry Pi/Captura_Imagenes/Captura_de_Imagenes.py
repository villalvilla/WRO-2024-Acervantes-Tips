from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import time

camara = PiCamera()
w = 640
h = 480
camara.resolution = (w, h)
capNoProcesada = PiRGBArray(camara)

time.sleep(0.3)

camara.capture(capNoProcesada, format="bgr")
imagen = capNoProcesada.array

cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Imagen', w,h)
cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.imwrite("imagen.jpg", imagen)
cv2.destroyAllWindows()
