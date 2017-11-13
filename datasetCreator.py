import cv2
import numpy as numpy

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture('1.avi');
id=input('enter user id ')
sampleNumber=0;
while (True):
	ret,img=cam.read();
	grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(grayImg,1.3,5);
	for (x,y,w,h) in faces:
		sampleNumber+=1;
		cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNumber)+".jpg",grayImg[y:y+h,x:x+w])
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2);
		cv2.waitKey(100);
	cv2.imshow("Face",img);
	cv2.waitKey(1)
	if(sampleNumber>20):
		break;
cam.release()
cv2.destroyAllWindows()