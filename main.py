import cv2
import time

# livefeed = cv2.VideoCapture(0)
# check, frame = livefeed.read()
# time.sleep(1)
# cv2.imwrite("testframe.png", frame)
# time.sleep(1)
# check, frame = livefeed.read()
# time.sleep(1)
# cv2.imwrite("testframe2.png", frame)
# time.sleep(1)
# check, frame = livefeed.read()
# time.sleep(1)
# cv2.imwrite("testframe3.png", frame)
# time.sleep(1)

livefeed = cv2.VideoCapture(0)
time.sleep(3)

while True:
    check, frame = livefeed.read()
    cv2.imshow("My Video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

livefeed.release()