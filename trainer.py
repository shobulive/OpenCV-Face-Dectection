import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create();
path='dataSet'

def getImagesWithId(path):
	imgPaths=[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
	faces=[]
	IDs=[]
	for imgPath in imgPaths:
		faceImg=Image.open(imgPath).convert('L');
		faceNp=np.array(faceImg,'uint8');
		ID=int(os.path.split(imgPath)[-1].split('.')[1]);
		print(ID)
		faces.append(faceNp);
		IDs.append(ID);
		cv2.imshow("tranining",faceNp);
		cv2.waitKey(10);
	return IDs,faces;
Identities,faces=getImagesWithId(path);
recognizer.train(faces,np.array(Identities))
recognizer.write('recognizer/traniningData.yml');
cv2.destroyAllWindows()