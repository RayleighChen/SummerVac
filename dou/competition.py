# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:19:30 2017

@author: asus
"""

import numpy as np
import pandas as pd

#数据读取
traindata=pd.read_excel(r'training .xlsx',names = ['y','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12'])
#数据剔除
#traindata=traindata.ix[traindata.y>1,0:]

y=traindata.iloc[0:,0]
x=traindata.iloc[0:,1:]



#尺度归一
def normalization(x):
    x = (x- np.min(x))/(np.max(x) - np.min(x));
    return x;
y_train=np.array(normalization(y))
x_train=np.array(normalization(x))

a=np.ones(len(x_train))
xfinal=np.column_stack((x_train,a))

#训练数据
lr=0.0001
w=np.array([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
#w=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])
##批量梯度
for i in range(10000):
    w = w - 2*lr * (-xfinal).T.dot(y_train - xfinal.dot(w))

#随机梯度下降
#for i in range(len(x_train)):
#    w=w-lr*2*(y_train[i]-(w[0]+w*x[i]))*(-x[i])
#    
#测试数据
textdata=pd.read_excel(r'testing.xlsx',names = ['y','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12'])
yt=textdata.iloc[0:,0]
xt=textdata.iloc[0:,1:]

#y_text=np.array(normalization(yt))
x_text=np.array(normalization(xt))
a1=np.ones(len(x_text))
xtt=np.column_stack((x_text,a1))
ytt=(xtt.dot(w))*(np.max(yt) - np.min(yt))+np.min(yt)
print ('RMSE',np.sqrt(np.sum((yt-ytt)**2/len(xtt))))