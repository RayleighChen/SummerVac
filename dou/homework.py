# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 12:48:48 2017

@author: asus
"""
import xlrd
import numpy as np
data = xlrd.open_workbook('hw-linear_regression.xlsx')
table=data.sheets()[0]
def Normalization(x):
    x = (x- np.min(x))/(np.max(x) - np.min(x));
    return x;
y_y=table.col_values(1)
y_1=np.array(y_y[4:24])
y=Normalization(y_1)



x1_x1=table.col_values(2)
x1_1=np.array(x1_x1[4:24])
x1=Normalization(x1_1)

x2_x2=table.col_values(2)
x2_1=np.array(x2_x2[4:24])
x2=Normalization(x2_1)

x3_x3=table.col_values(2)
x3_1=np.array(x3_x3[4:24])
x3=Normalization(x3_1)

x4_x4=table.col_values(2)
x4_1=np.array(x4_x4[4:24])
x4=Normalization(x4_1)

learning_rate=0.01
w0,w1,w2,w3,w4=0,0,0,0,0
train_num=1e+08
for i in range(20):
    w0=w0-learning_rate*np.sum((y-(w0+w1*x1+w2*x2+w3*x3+w4*x4))*(-1))
    w1=w1-learning_rate*np.sum((y-(w0+w1*x1+w2*x2+w3*x3+w4*x4))*(-x1))
    w2=w2-learning_rate*np.sum((y-(w0+w1*x1+w2*x2+w3*x3+w4*x4))*(-x2))
    w3=w3-learning_rate*np.sum((y-(w0+w1*x1+w2*x2+w3*x3+w4*x4))*(-x3))
    w4=w4-learning_rate*np.sum((y-(w0+w1*x1+w2*x2+w3*x3+w4*x4))*(-x4))
#    print(i,'  ',np.sum((y-(w0+w1*x1+w2*x2+w3*x3+w4*x4))**2))

y_t=np.array(y_y[25:])
#y_forcharge=Normalization(y_t)

x1_t=np.array(x1_x1[25:])
x1t=Normalization(x1_t)

x2_t=np.array(x2_x2[25:])
x2t=Normalization(x2_t)

x3_t=np.array(x3_x3[25:])
x3t=Normalization(x3_t)

x4_t=np.array(x4_x4[25:])
x4t=Normalization(x4_t)

yt=w0+w1*x1t+w2*x2t+w3*x3t+w4*x4t
ytest=yt*(np.max(y_1)-np.min(y_1))+np.min(y_1)

print('test_y',ytest)
print('test_erro: ',np.sum((y_t-ytest)**2))