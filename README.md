# cv2-camera-face-analisis
![python](https://img.shields.io/badge/python-3.8.10-green?style=flat-square)
![pip](https://img.shields.io/badge/pip-20.0.2-yellowgreen?style=flat-square)
![virtualenv](https://img.shields.io/badge/virtualenv-20.0.17-yellowgreen?style=flat-square)
![opencv-python](https://img.shields.io/badge/opencv--python-4.5.2-blue?style=flat-square)
![numpy](https://img.shields.io/badge/numpy-1.19.5-blue?style=flat-square)
![tensorflow](https://img.shields.io/badge/tensorflow-2.5.0-orange?style=flat-square)
![keras](https://img.shields.io/badge/keras-2.5.0-orange?style=flat-square)
### How to use
First create virtual environment (personally I used `virtualenv` tool) and activate it. Then install all packages shown above. Make sure your camera 
is not being used by any other program at the moment. When you are finished, you can run `camera.py` script in terminal using `python3 camera.py` command.
No additional arguments are needed. After a few seconds of initialization program will show live camera footage. Script will be looking for faces on every frame
of the video. When it will find one, it will track it as long as it's possible. After breaking the connection between face and program (for ex. by covering 
your face with facemask), script will search for a new face to analyse. Program analyses face to determine its gender, age group and ethnicity. Program will show
camera footage with predictions written above when face is found. Accuracy of predictions is divided into groups:`gender: 98%` `age group: 70%` `ethnicity: 85%`.
### Camera
### Functions
### Models
