import numpy as np
import cv2
import csv


for i in range(2,501):
    if 10-i>0:
        string='000%d'%i
    elif 100-i>0:
        string='00%d'%i
    else :
        string='0%d'%i
    depth_image = 'dataset5/E/l/depth_11_'+string+'.png'
    color_image = 'dataset5/E/l/color_11_'+string+'.png'
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
    hand_data = [[0 for i in range(128)] for j in range(128)]
    for i in range(128):
        for j in range(128):
            if (len(img_gray) > i):
                if (len(img_gray[0]) > j):
                    hand_data[i][j] = img_gray[i][j]


    cv2.imshow('depth', imgD);

    cv2.imshow('color image', img_color)
    cv2.imshow('gray image', img_gray)
    csvname='handdata/E/l/'+string+'.csv'
    with open(csvname, 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile, delimiter='\n')
        datawriter.writerow(hand_data)

    #cv2.imwrite('result.png', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindow()
