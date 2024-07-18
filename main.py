import time
import cv2

video = cv2.VideoCapture(0)

# to avoid blank frames and give camera time to load
# if its inside while loop the video lags for every second
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow("My video", frame)

    # create keyboard key object
    key = cv2.waitKey(1)

    # if user press q key it breaks the video i.e, stops the program
    if key == ord("q"):
        break

video.release()