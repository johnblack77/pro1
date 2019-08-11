import math
import cv2
import numpy as np
x=[2,4]
center=[0,0]
r=math.sqrt(math.pow(x[0]-center[0],2)+math.pow(x[1]-center[1],2))
theta=math.atan2(x[1]-center[1],x[0]-center[0])/math.pi*180#转换为角度
print (r,theta)



def hough(img):
    ROW, COL = img.shape()
    for i in range(ROW):
        for j in range(COL):
            if img[i][j] == 1:
                for k in range(-100,100):

