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

cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', w,h)

for frame in camara.capture_continuous(capNoProcesada, format="bgr", use_video_port=True):
    imagen = frame.array
    cv2.imshow("Frame", imagen)
    capNoProcesada.truncate(0)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
