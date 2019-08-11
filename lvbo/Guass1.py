
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import *

def Guass( ksize , sigma):
    pi = 3.1415926
    center = int(ksize / 2)
    window = np.zeros((ksize,ksize))
    for i in range(ksize):
        x2 = (i - center)*(i - center)
        for j in range(ksize):
            y2 = (j - center)  * (j - center)
            g = math.exp(-(x2 + y2) / (2 * sigma * sigma))
            g /= 2 * pi * sigma
            window[i][j] = g
    k = 1 / window[0][0]
    for i in range(ksize):
        for j in range(ksize):
            window[i][j] *= k
    return window/16

def saltpepper(img,n):
    m=int((img.shape[0]*img.shape[1])*n)
    for a in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=255
        elif img.ndim==3:
            img[j,i,0]=255
            img[j,i,1]=255
            img[j,i,2]=255
    for b in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=0
        elif img.ndim==3:
            img[j,i,0]=0
            img[j,i,1]=0
            img[j,i,2]=0
    return img

def ma():
    RGB_data = cv2.imread('lena.png',cv2.IMREAD_COLOR)
    Gray_data = cv2.cvtColor(RGB_data, cv2.COLOR_BGR2GRAY)
    print(Gray_data)
    [ROW,COL] = Gray_data.shape

    plt.subplot(1,3,1)
    plt.imshow(Gray_data,cmap='gray')

    imgn = saltpepper(Gray_data,0.01)
    plt.subplot(1,3,2)
    plt.imshow(imgn,cmap='gray')

    k = 5
    o = 1.4
    t=0
    result = np.zeros((ROW,COL))
    tmp = np.zeros((k,k))
    win = Guass(k,o)
    for i in range(ROW-k+1 ):
        for j in range(COL-k+1 ):
            for p1 in range(k):
                for p2 in range(k):
                    tmp[p1][p2] = imgn[i+p1][j+p2]

            result[i][j] =sum(multiply(tmp, win))
            #




    plt.subplot(1,3,3)
    plt.imshow(result,cmap='gray')

    plt.show()


if __name__ == '__main__':
    ma()