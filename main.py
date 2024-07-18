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

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    #to remove noise ,None - Configuration array
    dilated_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", dilated_frame)

    # to create contours
    contours, check = cv2.findContours(dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if the contour is smaller than other contour we say its a fake object
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue

        # to create rectangle around the objects
        x, y, w, h = cv2.boundingRect(contour)
        # rectangle has 5 arguments
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    #display original frame
    cv2.imshow("Video", frame)

    # create keyboard key object
    key = cv2.waitKey(1)

    # if user press q key it breaks the video i.e, stops the program
    if key == ord("q"):
        break

video.release()