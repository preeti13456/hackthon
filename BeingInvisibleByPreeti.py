import os
os.path
os.system("date")
import cv2
import numpy as np
import signal
import time
import matplotlib.pyplot as plt
from IPython import display
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
time.sleep(2)

background = 0
 
 # Capturing the background
for i in range(30): 
    ret, background = cap.read()
    
 #Capturing the image    
while(cap.isOpened()):
    
    ret, img = cap.read()
    
    
    if not ret:
        break
    #HSV values    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #HSB
    
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 =cv2.inRange(hsv, lower_red, upper_red) #eperating cloak part
    
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 =cv2.inRange(hsv, lower_red, upper_red) #eperating cloak part
    
    mask1 = mask1 + mask2
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,
                             np.ones((3,3), np.unit8), iterations=2)#noise removal
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,
                             np.ones((3,3), np.unit8), iterations=1)
        
    mask2 = cv2.bitwise_not(mask1)
    
    res1 = cv2.bitwise_and(background, background, mask=mask1) #used for segmentation of the color
    res2 = cv2.bitwise_and(background, background, mask=mask2) #used to substitute the cloak part
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow("Eureka!!", final_output)
    k = cv2.waitKey(10) 
    if k == 27:
        break
cap.release()        
cv2.destroyAllWindows()
    
