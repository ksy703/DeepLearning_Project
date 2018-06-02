import numpy as np
import cv2
import csv

imgD = cv2.imread('dataset5/D/a/depth_0_0422.png',1)


img_color = cv2.imread('dataset5/D/a/color_0_0422.png', cv2.IMREAD_COLOR)
img_ycrcb=cv2.cvtColor(img_color,cv2.COLOR_BGR2YCrCb)
img_gray=cv2.inRange(img_ycrcb,np.array([0,133,77]),np.array([255,173,127]))

for i in range(len(imgD)):
    for j in range(len(imgD[0])):

        if(imgD[i][j][0]>3):
            img_gray[i][j]=0
        if(imgD[i][j][0]==0):
            img_gray[i][j]=0
        print(imgD[i][j])
        print(img_gray[i][j])

_,img=cv2.threshold(img_gray,60,255,cv2.THRESH_BINARY)
img=cv2.morphologyEx(img, cv2.MORPH_ERODE, np.array((3,3),np.uint8), iterations=2)
img_gray=cv2.morphologyEx(img, cv2.MORPH_OPEN, np.array([7, 7, 1]), iterations=2)
#img_gray=cv2.morphologyEx(img, cv2.MORPH_CLOSE,np.array([9, 9, 1]), iterations=2)
#cv2.medianBlur(img, 15)

cv2.erode(img_gray,np.ones((5,5), np.uint8),1,2)

_,contours,_=cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
max_area = 100
ci = 0
for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt)
    if (area > max_area):
        max_area = area
        ci = i

cv2.drawContours(img_color,contours, ci, (0, 255, 255), 2)



cv2.imshow('depth',imgD);


cv2.imshow('color image', img_color)
cv2.imshow('gray image', img_gray)

cv2.imwrite('result.jpg', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindow() 