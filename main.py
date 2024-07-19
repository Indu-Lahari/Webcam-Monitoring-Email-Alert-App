import glob
import time
import cv2
from gmail import send_mail
video = cv2.VideoCapture(0)

# to avoid blank frames and give camera time to load; if its inside while loop, the video lags for every second
time.sleep(1)

first_frame = None
status_list = []
count = 1

while True:
    status = 0
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
    # if the contour is smaller than other contour we say it's a fake object
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue

        # to create rectangle around the objects
        x, y, w, h = cv2.boundingRect(contour)
        # rectangle has 5 arguments
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        #Trigger action , used any() as it is ambiguous(error)
        if rectangle.any():
            status = 1
            # to store images from video. Here img.png is static so f{count} males it dynamic
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            # Getting only middle or one image
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]


    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        send_mail(image_with_object)

    print(status_list)

    #display original frame
    cv2.imshow("Video", frame)

    # create keyboard key object
    key = cv2.waitKey(1)

    # if user press q key it breaks the video i.e, stops the program
    if key == ord("q"):
        break

video.release()