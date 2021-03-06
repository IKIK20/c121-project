import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

import time
time.sleep(2)

frame=cv2.resize(frame, (640,480))
img=cv2.resize(img, (640,480))

u_black= np.array([104,153,70])
l_black= np.array([30,30,0])

mask=cv2.inRange(frame, l_black, u_black)
res= cv2.bitwise_and(frame,frame, mask=mask)


bg = 0
for i in range(60):
    ret, bg = cap.read()

import numpy as np
bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
    ret,img= cap.read()
    if not ret:
        break
    
    img= np.flip(img, axis=1)


cap.release()
cv2.destroyAllWindows()
