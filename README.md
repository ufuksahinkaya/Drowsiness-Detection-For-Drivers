## Drowsiness Detection for Drivers

This Python project detects whether drivers are yawning or falling asleep by monitoring their eye and mouth movements. The project uses the dlib library to detect and track facial features. If the driver appears drowsy or yawns, an alarm sound is played.

## Purpose
The purpose of this system is to enhance traffic safety and ensure drivers can travel more safely, especially on long journeys. By detecting signs of drowsiness early, it aims to prevent accidents.

## Features
- Real-time face and eye detection
- Drowsiness detection based on the duration of closed eyes
- Yawning detection based on mouth movements
- Alerts the driver with a warning message and alarm sound

## Requirements
- Python 3.x
- OpenCV
- dlib
- pygame

## Installation
1. Install the required Python packages:
    ```bash
    pip install opencv-python dlib pygame
    ```
2. Download the dlib facial landmark predictor file and place it in the main directory of your project:
    [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

3. Place the project file and alarm sound file in the same directory.

## Usage
To run the project, use the following command:
```bash
python drowsiness_detection.py
```
The code will start working in real-time as soon as the camera is opened.

### Functions
- `eyes()`: Calculates the eye aspect ratio.
- `lips()`: Calculates the distance between the lips.
- `send_alert()`: Displays a warning message and plays an alarm sound.
- `finish()`: Releases the camera and closes all windows.

### Main Loop
As long as the camera is open, face detection is performed on each frame, and eye and mouth movements are monitored. If the eyes remain closed for a certain period or the mouth opens to a certain extent, an alert is triggered.

#Eye Aspect Ratio (EAR) Formula
The Eye Aspect Ratio (EAR) formula is used to determine the openness of the eyes by calculating the ratio of vertical distances to the horizontal distance of the eye. This ratio helps in detecting whether the eyes are open or closed, which is crucial for drowsiness detection.
[](images.assest\EAR.png)
[](images.assest\eye.png)
## Contributing
If you want to contribute, please send a pull request or create an issue.

## License
This project is licensed under the MIT License.
