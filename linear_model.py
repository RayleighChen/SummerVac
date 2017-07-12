# -*- coding: utf-8 -*-

import os
import sys
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#from sklearn.utils import shuffle

path = os.path.abspath(os.path.dirname(sys.argv[0]))   #获得当前文件路径
data = pd.read_excel(path+"/hw_linear_regression.xlsx",header=None)

def scale(X):
    X = (X - np.min(X))/(np.max(X)-np.min(X))
    return X
def loss(x,y):
    return (np.sum((x-y)**2))/y.shape[0]
def stack(X):
     X= np.hstack((np.ones((X.shape[0],1)), X))
     return X
data1 = data.ix[4:31,1:5]

data2 = shuffle (data1) 
data_X = data.ix[4:31,2:5]
data_y = data.ix[4:31,1]
data_X = scale (data_X)

X_train = data_X.loc[4:23,2:5]
y_train = data_y.loc[4:23]

X_test = (data_X.ix[24:31,2:5])
y_test = (data_y.ix[24:31])



learning_rate = 0.001
iteration = 20


X_train = stack(X_train)
X_test = stack(X_test)
w = np.random.random(5)
loss_error=[]
for i in range(iteration):
    print ("iter %d error: %f " %(i,loss(X_train.dot(w), y_train)))
    w = w- learning_rate*2*(y_train - X_train.dot(w)).T.dot(-X_train)
    loss_error.append(loss(X_train.dot(w), y_train))

test_error = loss(X_test.dot(w), y_test)
print ("test error: %f " %(loss(X_test.dot(w), y_test)))

plt.plot(loss_error)
plt.scatter(50,test_error,c='r')







