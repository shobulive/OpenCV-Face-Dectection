# OpenCV-Face-Dectection
Face Detection System using OpenCV, TensorFlow and python.

## Dependencies
 * OpenCV
 * TensorFlow 
 * python
 * Pillow
 
## How to use

**1. Install python3** 

Use the following command:

>$ brew install python3

check using

>python --version

**2. Install OpenCV** 

Install pip using following command:

>$ sudo easy_install pip

Then, install opencv using this command

>$ pip install opencv-python

check using,

>$ python

It will load python like this

Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

Now input the following

>import cv2

if it works fine then openCV installed

**3. Install TensorFlow**

Please follow this link --> [Install TensorFlow](https://www.tensorflow.org/install/)

**4. Install Pillow**

Input the following command

>$ pip install pillow

**5. Run the project**

First clone the repository

>$ git clone https://github.com/shubham56/OpenCV-Face-Dectection.git

>$ cd OpenCV-Face-Dectection

First you need to train the system by inputting the dataset:

>$ python datsetCreator.py

it will prompt you to enter the id, enter any integer value from 0.

Then,it will capture images of the subject using Web Cam.

then to build the recognizer using given training data run, 

>$ python trainer.py

Now to check the system run,

>$ python faceDetection.py

It will display the id for recognized face and unknown for unrecognized face.

## Credits
* [TensorFlow](https://www.tensorflow.org/) by Google
* [Python](https://www.python.org/)
* [OpenCV](openCv.org)
* [Pillow](https://python-pillow.org/)
