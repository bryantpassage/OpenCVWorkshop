
import numpy as np # First we need our imports
import cv2


# Get the video
capture = cv2.VideoCapture(0) # 0 indicates that it is continuous

# now we loop the video feed
while(True): # True makes it forever
    ret, frame = capture.read() # read a frame

    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow("Frame",frame)


    ch = cv2.waitKey(1) #Indicated to run every 1 second
    if ch & 0xFF == ord('q'): # Our statement to break out of the loop
        break


capture.release() # Dont forget this line
cv2.destroyAllWindows()
