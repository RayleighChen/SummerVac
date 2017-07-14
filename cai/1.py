import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression

train = pd.read_csv('C:/Users/caijiawen/Desktop/train.csv')
test = pd.read_csv('C:/Users/caijiawen/Desktop/testt.csv')
rate=0.00001
#train=pd.double(train)
train=train.astype(float)
test=test.astype(float)
n=pd.Series([100,100,100,10000,1000,1000,10,10,1000000,100000,10,1000,10000000])
w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12=0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01 
b=0.01
for i in range(train.shape[0]):
    for j in range (13):
        train.iat[i,j]/=n[j]
for i in range(test.shape[0]):
    for j in range (13):
        test.iat[i,j]/=n[j]
for i in range (4000):
    
    t=train['Y']-(b+train['1']*w1+train['2']*w2+train['3']*w3+train['4']*w4+train['5']*w5+train['6']*w6+train['7']*w7+train['8']*w8+train['9']*w9+train['10']*w10+train['11']*w11+train['12']*w12)
    w1=w1-rate*np.sum(2*(t*(-train['1'])))
    w2=w2-rate*np.sum(2*(t*(-train['2'])))
    w3=w3-rate*np.sum(2*(t*(-train['3'])))
    w4=w4-rate*np.sum(2*(t*(-train['4'])))
    w5=w5-rate*np.sum(2*(t*(-train['5'])))
    w6=w6-rate*np.sum(2*(t*(-train['6'])))
    w7=w7-rate*np.sum(2*(t*(-train['7'])))
    w8=w8-rate*np.sum(2*(t*(-train['8'])))
    w9=w9-rate*np.sum(2*(t*(-train['9'])))
    w10=w10-rate*np.sum(2*(t*(-train['10'])))
    w11=w11-rate*np.sum(2*(t*(-train['11'])))
    w12=w12-rate*np.sum(2*(t*(-train['12'])))
    b=b-rate*np.sum(2*(t*(-1)))
ans=0
print(w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12)
for i in range(test.shape[0]):
    
    t=(b+test.iat[i,1]*w1+test.iat[i,2]*w2+test.iat[i,3]*w3+test.iat[i,4]*w4+test.iat[i,5]*w5+test.iat[i,6]*w6+test.iat[i,7]*w7+test.iat[i,8]*w8+test.iat[i,9]*w9+test.iat[i,10]*w10+test.iat[i,11]*w11+test.iat[i,12]*w12)
    t=t*100
    if(test.iat[i,12]*10000000<100):
        t=0
#         print(test.iat[i,12],test.iat[i,0]*100)
    ans+=((t-test.iat[i,0]*100)**2)
print('均方差 %.2f' % math.sqrt(ans/test.shape[0]))
