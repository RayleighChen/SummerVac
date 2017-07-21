# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 10:53:07 2017

@author: asus
"""

import theano
from theano import tensor as T
from theano.tensor.nnet import conv2d
import numpy as np

x=T.ivector('x')
w=T.ivector('w')
w=np.array([1,0,0,1])
w=w.reshape((1,1,2,2))
input=T.tensor4(name='input')


w = theano.shared( np.asarray(w,dtype=input.dtype), name ='w')


conv_out=conv2d(input,w)

f=theano.function([input],conv_out)

x=np.array([1,2,3,4,5,6,7,8,9])
x=x.reshape((1,1,3,3))

print(f(x))