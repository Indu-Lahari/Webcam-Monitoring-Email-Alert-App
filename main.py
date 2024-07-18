import time

import cv2


video = cv2.VideoCapture(0)
check, frame = video.read()
time.sleep(1)
check2, frame2 = video.read()
time.sleep(1)
check3, frame3 = video.read()
time.sleep(1)

print(video)
print(frame)