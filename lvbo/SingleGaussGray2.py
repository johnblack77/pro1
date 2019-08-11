import cv2
import numpy as np

img1 = cv2.imread('aggregate/0329.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('aggregate/0330.jpg',cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('aggregate/0331.jpg',cv2.IMREAD_GRAYSCALE)
alpha = 0.03  # 更新率/背景建模alpha值
lamda = 2.5 * 1.2  # 背景更新参数
h,w=img1.shape
img_u=np.zeros((h,w),dtype=np.float)#高斯函数的均值(背景)
img_d=np.zeros((h,w),dtype=np.float)#前景
img_std=np.zeros((h,w),dtype=np.float)#高斯函数的标准差
img_var=np.zeros((h,w),dtype=np.float)#高斯函数的方差
num = 332
for i in range(h):
    for j in range(w):
        img1_u=int(img1[i,j])
        img2_u=int(img2[i,j])
        img3_u=int(img3[i,j])
        img_u[i,j]=(img1_u+img2_u+img3_u)/3
        img_var[i,j]=20*20
        img_std[i,j]=20


print(len(img_var))
print(len(img_std))
for i in range(10):
    number = num + i
    string = 'aggregate/0' + str(number) + '.jpg'
    img = cv2.imread(string,cv2.IMREAD_GRAYSCALE)
    for i in range(h):
        for j in range(w):
            pixel_i=img[i,j]
            pixel_u=img_u[i,j]
            pixel_std=img_std[i,j]
            pixel_var=img_var[i,j]
            if abs(pixel_i-pixel_u)<lamda*pixel_std:
                #背景更新
                img_u[i,j]=(1-alpha)*pixel_u+alpha*pixel_i
                #方差更新
                img_var[i,j]=(1 - alpha) * pixel_var + alpha * pow((pixel_i - img_u[i,j]), 2)
                #标准差更新
                img_std[i,j]=pow(img_var[i,j],0.5)
                img_d[i, j] = 0
            else:
                img_d[i,j]=255
img_U=img_u.astype(np.uint8)

cv2.imshow('background ',img_U )
cv2.imshow('prospect ', img_d)
cv2.waitKey(0)
cv2.destroyAllWindows()