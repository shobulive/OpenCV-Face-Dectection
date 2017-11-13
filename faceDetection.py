import cv2
import numpy as numpy
import os
from PIL import Image

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read('./recognizer/traniningData.yml')
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
id=0;
while (True):
	ret,img=cam.read();
	grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(grayImg,1.3,5);
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2);
		id,conf=rec.predict(grayImg[y:y+h,x:x+w])
		if(conf>50)
		id="Unknown"
		cv2.putText(img,str(id),(x,y+h),font,2,200,2,8)
	cv2.imshow("Face",img);
	if(cv2.waitKey(1)==ord('q')):
		break;
cam.release()
cv2.destroyAllWindows()