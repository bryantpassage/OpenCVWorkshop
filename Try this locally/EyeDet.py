import numpy as np
import cv2
import matplotlib.pyplot as plt


capture = cv2.VideoCapture(0)
path = "haarcascade_eye.xml" #Important

eye_cascade = cv2.CascadeClassifier(path)


while True:

	#Capture each frame from video camera
	ret, frame = capture.read() # read a frame
	frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
	grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# Method from our cascade classifier that detects something
	eyes = eye_cascade.detectMultiScale(grayFrame, scaleFactor=1.02,minNeighbors=20,minSize=(10,10))

	for (x, y, w, h) in eyes:
		xc = (x + x+w)/2
		yc = (y + y+h)/2
		radius = w/2
		# Draws circle on screen
		cv2.circle(frame, (int(xc),int(yc)), int(radius), (255,0,0), 2)

	cv2.imshow("Image",frame)


	ch = cv2.waitKey(1) #Indicated to run every 1 second
	if ch & 0xFF == ord('q'): # Our statement to break out of the loop
	    break

capture.release() # Dont forget
cv2.destroyAllWindows()
