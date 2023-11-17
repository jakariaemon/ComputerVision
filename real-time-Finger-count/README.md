# Real-Time-Finger-Count

## Overview 
The Hand Tracking Application is a real-time solution for tracking and detecting the movement of hands. It can also identify the number of fingers being held up. The program is written in Python and utilizes the OpenCV and MediaPipe libraries to process video and recognize hand landmarks. The app also features a GUI built with the Gooey library, enhancing user experience and making the program more interactive. 

## How to run 
- Download as zip or git clone the repo.
- Extract it.
- Open Anaconda Prompt and navigate to the extracted directory.
- Now create a virtural enviroment. 
  ```
  conda create -n test_finger
  ```
- Now activate the environment.
  ```
  conda activate test_finger
  ```
- Now install requiremtns.
  ```
  pip install -r requiremnets.txt
  ```
- Now run the GUI version of the app.
  ```
  python app.py
  ```
- Now Click start and your webcam will turn on.
- Note: Please use upper of you hand. as the model most probably traind on upper side of hand data.


## Prerequisites:
- Python 3.x
- OpenCV
- MediaPipe
- Gooey
- A computer with a camera for video capture.

## Features:
- Real-Time Hand Tracking: The application processes video in real-time, tracking hand movements and landmarks.
- Finger Detection: The application can detect the number of fingers a user is holding up and display a corresponding image from a predefined directory.
- FPS Counter: The real-time processing frame rate (in Frames Per Second) is displayed on the application window.
- Interactive GUI: The Gooey library has been used to provide an interactive GUI, making the application more user-friendly.

# Working Principle 
The Hand Tracking Application primarily utilizes computer vision techniques powered by the OpenCV library and MediaPipe's hand solutions to detect, track, and analyze hand movements in real-time.
## Video Capture:
The application begins by capturing live video feed using a computer's camera. This is facilitated by the OpenCV function:
```
cap = cv2.VideoCapture(0)
```
Here, 0 usually refers to the default camera on the computer.
## Image Processing:
For the hand detection to work effectively, the RGB format is more suitable. Therefore, each frame from the video is converted from BGR to RGB:
```
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
## Hand Detection:
After converting the frame to RGB, it is passed to the MediaPipe's hand solution for processing:
```
self.results = self.hands.process(imgRGB)
```
MediaPipe processes the image and returns landmarks if hands are detected in the frame.
## Drawing Landmarks:
If hands are detected in the image, the application can draw the landmarks and their connections on the hands for visual representation. This is facilitated using MediaPipe's drawing utilities:
```
self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
```
## Finding Position:
For each detected hand, the application calculates the position of the landmarks. These positions are then scaled to match the dimensions of the captured frame:
```
cx, cy = int(lm.x * w), int(lm.y * h)
```
Here, lm.x and lm.y are the normalized positions of the landmark in the image, and w and h are the width and height of the image, respectively.
## Finger Detection:
Based on the landmarks' positions, the application determines which fingers are extended. This is done by comparing the y-coordinates of the finger tips with their respective lower joints. For instance, for the thumb, the application checks the x-coordinate:
```
if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
    fingers.append(1)
```
For other fingers, it checks the y-coordinate:
```
if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
    fingers.append(1)
```
A list, fingers, is populated with values 0 or 1, indicating which fingers are bent or extended, respectively.
## Overlay Images:
Depending on the number of fingers detected to be extended, a corresponding image from the finger directory is overlaid onto the video feed.
## Display:
The processed frame with all the drawings, finger count, and overlaid image is displayed in real-time using OpenCV's imshow function:
```
cv2.imshow("Image", img)
```
## Frame Rate Calculation:
For performance analysis and user information, the application calculates the frame rate (in frames per second) of the processed video and displays it on the video feed.
## User Interaction:
The Gooey library adds a user interface layer to the application. Before starting hand detection, the user interacts with the GUI, selecting the "Ready to Start" option.

## Conclusion:
The Hand Tracking Application is a combination of image processing, computer vision techniques, and GUI for user interaction. It leverages the capabilities of OpenCV and MediaPipe to provide real-time hand and finger tracking, making it suitable for a range of applications from gesture control to augmented reality.
