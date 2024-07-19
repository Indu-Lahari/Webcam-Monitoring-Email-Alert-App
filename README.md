# Build a Webcam Monitoring Email Alert App with Python

## Description

This project demonstrates how to build a webcam monitoring application that sends email alerts when motion is detected. The application captures video from the webcam, processes the frames to detect motion, and sends an email with an image attachment of the detected object.

## Process

1. **Capture Video**: The application captures video from the webcam using OpenCV.
2. **Frame Processing**: Each frame is converted to grayscale and then blurred using GaussianBlur to reduce noise.
3. **Motion Detection**: The difference between the first frame and the current frame is calculated to detect motion. If motion is detected, a rectangle is drawn around the detected object.
4. **Save Image**: When motion is detected, the frame is saved as an image file.
5. **Send Email**: If motion is detected and the status changes, an email with the captured image is sent using the smtplib library.
6. **Clean Up**: The application periodically cleans up the saved images to avoid clutter.

## Technology Used

- **Python**: The main programming language used for the application.
- **OpenCV**: For video capture and image processing.
- **smtplib**: For sending emails.
- **glob**: For file handling.
- **Pycharm IDE**: Used for developing and debugging the project.

## What I Learned from This Project

- **OpenCV Basics**: How to capture video from a webcam and process video frames.
- **Image Processing**: Techniques like converting to grayscale, blurring, and finding contours.
- **Motion Detection**: Using frame differencing and thresholding to detect motion.
- **Threading in Python**: How to use threading to run email sending and cleanup tasks concurrently.
- **Email Automation**: Sending emails with attachments using Python's smtplib.
- **Debugging and Error Handling**: Identifying and handling potential errors gracefully.
- **Project Organization**: Structuring a Python project with multiple files and modules.

## How to Run
- Clone the repository to your local machine.
- **Install the required libraries**: pip install opencv-python
- Update the email credentials in gmail.py.
- **Run the main.py**: python main.py
- Ensure the webcam is connected and functioning properly.
