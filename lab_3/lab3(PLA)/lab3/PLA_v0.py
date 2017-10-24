#!/usr/bin/env python

from numpy import *
import re

def substract_data(f_name):
    f = open(f_name)
    m = f.readlines()
    x = []
    y = []
    for i in range(len(m)):
        line = re.split(',| ',m[i])
        tmp = [1 for i in range(len(line))]
        for i in range(1,len(line)):
            tmp[i] = float(line[i-1])
        x.append(tmp)
        y.append(float(line[-1]))
        #augmenting vectos
    return array(x),array(y)

def origin_pla(x,y,w,k,row,col):
    for i in range(k):
        for j in range(row):
            tmp = sign(x[j].dot(w))
            if not tmp == y[i]:
                w = w + y[i]*x[i]
    return w


def cal_rate(x,y,w,row):
    predict = x.dot(w)
    tp = 0.0
    fn = 0.0
    tn = 0.0
    fp = 0.0
    ans = 0.0
    for i in range(row):
        if y[i] > 0:
            if predict[i] > 0:
                tp = tp + 1
                ans = ans+1
            else:
                fn = fn + 1
        else:
            if predict[i] > 0:
                fp = fp + 1
            else:
                tn = tn + 1
                ans = ans+1
    return ans/row,tp/row,fn/row,tn/row,fp/row


def pla(x,y,row,col):
    w0 = array([1.0 for i in range(col)])
    for i in range(1000):
        w = origin_pla(x,y,w0,i+1,row,col)
        [ans,tp,fn,tn,fp] = cal_rate(x,y,w,row)
        print(ans,tp,fn,tn,fp)



[x,y] = substract_data('/media/simon/Study/3-up/AI/lab3_PLA/lab3(PLA)/lab3/train.csv')
row = len(x)
col = len(x[0])

pla(x,y,row,col)


# for i in range(len(y)):
#     print(y[i])
