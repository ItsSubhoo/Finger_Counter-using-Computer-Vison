# Finger_Counter With OpenCV and MEdiapipe
This project uses OpenCV and Mediapipe to detect hand gestures from a webcam feed. It includes basic functionality to count open fingers on the detected hands and overlays the information on the video feed.

## Features
-  Real-time video capture from a webcam.
-   Python 3.x
- Hand landmark detection using Mediapipe.
- Finger count based on hand landmarks.
- FPS display for performance monitoring.
- Simple graphical interface with OpenCV.
## Dependencies
Ensure you have the following dependencies installed:

- Python 3
- OpenCV
- Mediapipe
- Comtypes
  
To install the required packages, use the following:
```bash
pip install opencv-python mediapipe 

```
Usage
To run the program, ensure you have a webcam connected to your system, then execute the script:

 ```bash

python hand_gesture_detection.py
```
A window will open, displaying the video feed from your webcam with the detected hand landmarks and finger count.

## Understanding the Code
-  The program captures video from a webcam.
-  Mediapipe's Hands solution detects hand landmarks.
 - Finger count is calculated by comparing specific landmarks' positions.
- The video feed is displayed with overlayed hand landmarks and finger count.
  - FPS is calculated and displayed for performance monitoring.
## Future Improvements
- Add support for additional hand gestures.
-Implement volume control based on hand gestures.
-Create a more detailed graphical interface.
-Add gesture-based interactions with other applications.
## Contribution
Contributions are welcome! Please feel free to open issues or create pull requests with suggestions, improvements, or bug fixes.

## Author
This project is maintained by me Subhajit Lai. You can contact me via email: iamsubhajitlai@gmail.com



