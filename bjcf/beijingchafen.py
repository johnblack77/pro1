import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 读取帧数
img_number = 96

# 各帧的集合
all_img = [np.array(Image.open('./image/input'+str(i+1)+'.jpg', 'r')) for i in range(img_number)]

# 帧的宽高
h = all_img[0].shape[0]
v = all_img[0].shape[1]

# 计算得到背景
back_img = np.zeros((h, v))
for single_img in all_img:
    back_img += single_img
back_img /= img_number

# 保存背景
Image.fromarray(back_img).convert('RGB').save('./out/background.jpg')

# 原视频与背景逐帧相减后取绝对值 得到前景
front_img = np.array([i - back_img for i in all_img])
front_img = front_img.__abs__()

# 前景二值化 设定阈值将前景像素值化为0或1
threshold_level = 50
threshold = np.full((h, v), threshold_level)
front_img = np.array([i < threshold for i in front_img], dtype=np.int8)*255

# 在原帧上抠图 得到真实的前景
front_img = np.fmax(np.array(front_img), all_img)

# 保存
for i in range(img_number):
    Image.fromarray(front_img[i]).convert('RGB').save('./out/'+str(i+1)+'.jpg')

# 显示
loc_h = 6
loc_v = int(img_number / loc_h)
for i in range(loc_h * loc_v):
    plt.subplot(loc_v, loc_h, i+1)
    plt.imshow(front_img[i], cmap='gray')
plt.show()




