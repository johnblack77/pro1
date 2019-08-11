# -*- coding: utf-8 -*-
import gensim
import codecs
#
#
# def main():
#     path_to_model = '000001.bin'
#     output_file = 'file.txt'
#     bin2txt(path_to_model, output_file)
#
#
# def bin2txt(path_to_model, output_file):
#     output = codecs.open(output_file, 'w', 'utf-8')
#     model = gensim.models.KeyedVectors.load_word2vec_format(path_to_model, binary=True)
#     print('Done loading Word2Vec!')
#     vocab = model.vocab
#     for item in vocab:
#         vector = list()
#         for dimension in model[item]:
#             vector.append(str(dimension))
#         vector_str = ",".join(vector)
#         line = item + "\t" + vector_str
#         output.writelines(line + "\n")  # 本来用的是write（）方法，但是结果出来换行效果不对。改成writelines（）方法后还没试过。
#     output.close()
#
#
# if __name__ == "__main__":
#     main()
#
#
# file = open('000001.bin', 'rb')
# i = 0
# for line in file:
#     print(line)

import numpy as np
import struct










# import numpy as np
# import struct
# # # 加载测试数据
# # # f = open('000001.bin','rb')
# # count = 0
# # for index, line in enumerate(open('000005.bin','rb')):
# #     count += 1
# # print(count)
# #
# # # 102500为文档中包含的数字个数，而一个浮点数占4个字节
# # # data_raw = struct.unpack('f'*102500,f.read(4*102500))
# # # f.close()
# # # verify_data =  np.asarray(data_raw).reshape(-1,4)
# # # print("jbfcn")
#
#
#
#
# # 加载测试数据
# f = open('000005.bin','rb')
#
# block = f.read(1024)
# print(block)
# print(len(block))
# a=struct.unpack('f'*1024,4*1024)
# f.close()
# print(block)