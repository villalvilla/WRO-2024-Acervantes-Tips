from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

camera = PiCamera()
w = 640
h = 480
camera.resolution = (w, h)
rawCapture = PiRGBArray(camera, size=(w, h))
time.sleep(0.3)

faceCascade = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    try:
        face = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))[0]
        (x, y, w, h) = face
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    except:
        pass
    cv2.imshow("Frame", image)
    rawCapture.truncate(0)
    key = cv2.waitKey(1) &amp; 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()