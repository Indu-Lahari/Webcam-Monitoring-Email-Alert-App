import time
import cv2

video = cv2.VideoCapture(0)

# to avoid blank frames and give camera time to load; if its inside while loop the video lags for every second
time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()

    # convert frames to grayscale frames to reduce the amount of data in matrices
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Another Method to make calculations more efficient is Gaussian Blur Method
    # 3 arguments are grayframe, blurness size and Standard Deviation
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    cv2.imshow("My video", delta_frame)

    # create keyboard key object
    key = cv2.waitKey(1)

    # if user press q key it breaks the video i.e, stops the program
    if key == ord("q"):
        break

video.release()