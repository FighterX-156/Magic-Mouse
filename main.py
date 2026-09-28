import cv2
capture=cv2.VideoCapture(0)
while True:
     _,frame=capture.read()
     cv2.imshow('Magic Frame',frame)
     cv2.waitKey(1)
     # trigger for camera off
     if cv2.waitKey(1) & 0xFF == ord ('q') :
         break
