import cv2
import numpy as np
from PIL import Image
import os

Temp_WIDTH = 0
STEP = 0
file_dir = ''
out_dir = ''
for root, dirs, files in os.walk(file_dir):
    in_str = root + files
    out = out_dir + files
    out = out[:-4]
    out += '/'
    img = cv2.imread(in_str, cv2.IMREAD_COLOR)
    height, width, cannel = img.shape
    # template = np.zeros((height, width, cannel),dtype=np.int8)

    for i in range(0, width - Temp_WIDTH, STEP):
        for j in range(0, height - Temp_WIDTH, STEP):
            template = img[i:i+Temp_WIDTH, j:j+Temp_WIDTH]
            Image.fromarray(template).convert('RGB').save(out + str(i) + '.jpg')