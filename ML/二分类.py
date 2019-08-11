import os
from numpy import *

os.chdir("E:\python learning\Machine Learning in Action\machinelearninginaction\Ch05")  # 设置路径


# 打开文件并逐行读取,每行的前两个值是特征值X1,X2，第3列是数据对应的标签
def loadDataSet():
    dataMat = [];
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()  # 去掉头尾的空格，并以空白字符为分隔符进行分割
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  # 并将dataMat矩阵的第一列设置为1
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat  # 输出特征矩阵和标签矩阵


dataArr, labelMat = loadDataSet()


# 定义sigmoid函数
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


# 定义梯度上升算法函数，其中dataMatIn参数为2维numpy数组，每列代表不同的特征，每行代表一个训练样本，labelMat为标签分类
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  # convert to NumPy matrix
    labelMat = mat(classLabels).transpose()  # convert to NumPy matrix
    m, n = shape(dataMatrix)  # 获取矩阵的行和列

    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))  # n为矩阵dataMatIn的列数，也就是变量的个数
    for k in range(maxCycles):  # heavy on matrix operations
        h = sigmoid(dataMatrix * weights)  # matrix mult,计算z值
        error = (labelMat - h)  # vector subtraction，计算预测值域实际值的偏差
        weights = weights + alpha * dataMatrix.transpose() * error  # matrix mult  #梯度下降算法，找出最佳的参数
    return weights


# 计算参数
weights = gradAscent(dataArr, labelMat)


# 画出决策边界：画出数据集和logistic回归最佳拟合直线的函数
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()  # 导入数据
    dataArr = array(dataMat)  # dataMat转换为数组
    n = shape(dataArr)[0]
    xcord1 = [];
    ycord1 = []
    xcord2 = [];
    ycord2 = []

    # 将数据按类别分类
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1]);
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]);
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-wei[0] - wei[1] * x) / wei[2]
    ax.plot(x, y)
    plt.xlabel('X1');
    plt.ylabel('X2');
    plt.show()


plotBestFit(weights.getA())

