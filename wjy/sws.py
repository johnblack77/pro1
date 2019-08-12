import cv2
import numpy as np
from PIL import Image
import os

Temp_WIDTH = 28
STEP = 4
file_dir = '/Users/john/PycharmProjects/pro1/data1/t1'
out_dir = '/Users/john/PycharmProjects/pro1/data1/t1'
os.mkdir(out_dir+'/out')
for root, dirs, files in os.walk(file_dir):
    for tmp in files:
        c=0
        os.mkdir(out_dir + '/out/'+tmp[:-4])
        in_str = root +'/' + tmp
        out = out_dir+'/out/' + tmp
        out = out[:-4]
        out += '/'
        print(in_str)
        img = cv2.imread(in_str, cv2.IMREAD_ANYCOLOR)
        height, width, cannel = img.shape
        # template = np.zeros((height, width, cannel),dtype=np.int8)
        for i in range(0, width - Temp_WIDTH, STEP):
            for j in range(0, height - Temp_WIDTH, STEP):
                template = img[i:i+Temp_WIDTH, j:j+Temp_WIDTH]
                Image.fromarray(template).convert('RGB').save(out + str(c) + 'png')
                c+=1