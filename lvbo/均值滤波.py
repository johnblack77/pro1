import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


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


RGB_data = cv2.imread('sws.jpg',cv2.IMREAD_COLOR)

B_data,G_data,R_data=cv2.split(RGB_data)
B_data = RGB_data[:,:,0]
G_data = RGB_data[:,:,1]
R_data = RGB_data[:,:,2]

[ROW,COL, DIM] = RGB_data.shape
Median_Img = np.zeros((ROW,COL))
Y_data = np.zeros((ROW,COL))
Cb_data = np.zeros((ROW,COL))
Cr_data = np.zeros((ROW,COL))
Gray_data = RGB_data

for r in range(ROW):
    for c in range(COL):
        Y_data[r, c] = 0.299*R_data[r, c] + 0.587*G_data[r, c] + 0.114*B_data[r, c];
        Cb_data[r, c] = -0.172*R_data[r, c] - 0.339*G_data[r, c] + 0.511*B_data[r, c] + 128;
        Cr_data[r, c] = 0.511*R_data[r, c] - 0.428*G_data[r, c] - 0.083*B_data[r, c] + 128;

Gray_data[:,:,0]=Y_data
Gray_data[:,:,1]=Y_data
Gray_data[:,:,2]=Y_data

plt.subplot(1,3,1)
plt.imshow(Gray_data)

imgn = saltpepper(Gray_data,0.01)

plt.subplot(1,3,2)
plt.imshow(imgn)

Median_Img = np.zeros((ROW,COL))
for r in range(1,ROW-1):
    for c in range(1,COL-1):
        median3x3 =[[imgn[r-1,c-1],imgn[r-1,c],imgn[r-1,c+1]],
                    [imgn[r,c-1],imgn[r,c],imgn[r,c+1]],
                    [imgn[r+1,c-1], imgn[r+1,c],imgn[r+1,c+1]]]
        Median_Img[r, c] = np.array(median3x3).mean()

plt.subplot(1,3,3)
plt.imshow(Median_Img,cmap='gray')

plt.show()