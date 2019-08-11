import numpy as np
import struct
# 加载测试数据
f = open('000001.bin','rb')
# 102500为文档中包含的数字个数，而一个浮点数占4个字节
data_raw = struct.unpack('f'*102500,f.read(4*102500))
f.close()
verify_data =  np.asarray(data_raw).reshape(-1,4)
print(verify_data)
print('ddxigj')