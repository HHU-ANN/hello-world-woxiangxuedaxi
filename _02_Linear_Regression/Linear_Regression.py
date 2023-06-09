# 最终在main函数中传入一个维度为6的numpy数组，输出预测值

import os

try:
    import numpy as np
except ImportError as e:
    os.system("sudo pip3 install numpy")
    import numpy as np

def ridge(data):
    x,y = read_data()
    t = 0.1
    weight = np.matmul(np.linal.inv(np.matmul(x.T,x)+t*np.eye()),np.matmul(x.T,y))
    return weight @ data


def lasso(data):
    a = 0.01
    t = 0.1
    x,y = read_data()
    min_max_scaler = preprocessing.MinMaxScaler()
    x = min_max_scaler.fit_transform(x)
    y = min_max_scaler.fit_transform(y)
    weight = weight - a*np.matmul(np.linal.inv(np.matmul(x.T,x)),np.matmul(x.T,y)-t/2)
    return weight @ data

def read_data(path='./data/exp02/'):
    x = np.load(path + 'X_train.npy')
    y = np.load(path + 'y_train.npy')
    return x, y

