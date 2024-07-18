import cv2

video = cv2.VideoCapture(0)
check, frame = video.read()

print(video)
print(frame)