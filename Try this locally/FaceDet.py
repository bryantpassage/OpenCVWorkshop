import numpy as np
import cv2
import matplotlib.pyplot as plt


capture = cv2.VideoCapture(0)

path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path)


while True:

	#Capture each frame from video camera
	ret, frame = capture.read() # read a frame
	frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

	grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# Method from our cascade classifier that detects something
	faces = face_cascade.detectMultiScale(grayFrame, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))

	for (x, y, w, h) in faces:
		 # Draws rectangles on our faces
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

	cv2.imshow("Image",frame)
	ch = cv2.waitKey(1) #Indicated to run every 1 second
	if ch & 0xFF == ord('q'): # Our statement to break out of the loop
	    break




capture.release() # Dont forget
cv2.destroyAllWindows()
