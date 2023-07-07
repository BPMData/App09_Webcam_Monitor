import cv2
import time

livefeed = cv2.VideoCapture(0)
check, frame = livefeed.read()
time.sleep(1)
cv2.imwrite("testframe.png", frame)
time.sleep(1)
check, frame = livefeed.read()
time.sleep(1)
cv2.imwrite("testframe2.png", frame)
time.sleep(1)
check, frame = livefeed.read()
time.sleep(1)
cv2.imwrite("testframe3.png", frame)
time.sleep(1)