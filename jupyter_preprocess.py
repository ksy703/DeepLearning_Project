import numpy as np
import tensorflow as tf
import cv2
import csv
import pandas as pd
import matplotlib.pyplot as plt

imgs = np.zeros((499, 128,128))
labels = np.zeros((499, 24))

indices = [0, 1, 2, 3, 4]
depth = 3
t = tf.one_hot(indices, depth)
t

for i in range(102,302):
    if 10-i>0:
        string='000%d'%i
    elif 100-i>0:
        string='00%d'%i
    else :
        string='0%d'%i
    alp='y'
    num='24'
    
    depth_image = '../data/dataset5/A/'+alp+'/depth_'+num+'_'+string+'.png'
    color_image = '../data/dataset5/A/'+alp+'/color_'+num+'_'+string+'.png'
    if i % 10 == 0:
        print(string)
    imgD = cv2.imread(depth_image, 1)
    img_color = cv2.imread(color_image, cv2.IMREAD_COLOR)
    img_ycrcb = cv2.cvtColor(img_color, cv2.COLOR_BGR2YCrCb)
    img_gray = cv2.inRange(img_ycrcb, np.array([0, 133, 77]), np.array([255, 173, 127]))

    for i in range(len(imgD)):
        for j in range(len(imgD[0])):

            if (imgD[i][j][0] > 3):
                img_gray[i][j] = 0
            if (imgD[i][j][0] == 0):
                img_gray[i][j] = 0

    _, img = cv2.threshold(img_gray, 60, 255, cv2.THRESH_BINARY)
    img = cv2.morphologyEx(img, cv2.MORPH_ERODE, np.array((3, 3), np.uint8), iterations=2)
    img_gray = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.array([7, 7, 1]), iterations=2)
    # img_gray=cv2.morphologyEx(img, cv2.MORPH_CLOSE,np.array([9, 9, 1]), iterations=2)
    # cv2.medianBlur(img, 15)
    hand_data=np.zeros(16385)
    hand_data[0]=int(num)
    for i in range(128):
        for j in range(128):
            if (len(img_gray) > i):
                if (len(img_gray[0]) > j):
                    hand_data[i*128+j+1]=img_gray[i][j]
            
    
#    imgs[i-2]=hand_data[i]
#     labels[i - 2] = tf.one_hot()
    
    df=pd.DataFrame(hand_data)
    f_name='A_'+alp+'_200.csv'
    df.T.to_csv(f_name, mode='a',header=None,index=None)
    
    


#     cv2.imshow('depth', imgD);

#     cv2.imshow('color image', img_color)
#     cv2.imshow('gray image', img_gray)
    #csvname='../data/l.csv'
    #with open(csvname, 'a', newline='') as csvfile:
        #datawriter = csv.writer(csvfile, delimiter=',')
        #datawriter.writerow(hand_data)

#     cv2.imwrite('result.png', img_gray)
plt.imshow(img_gray)
plt.title('Gray image')
# cv2.waitKey(0)
# cv2.destroyAllWindow()
