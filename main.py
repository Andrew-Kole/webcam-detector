import cv2
import time

video = cv2.VideoCapture(0)

check, frame = video.read()
time.sleep(1)

check1, frame1 = video.read()
time.sleep(1)

check2, frame2 = video.read()
time.sleep(1)

print(frame2)