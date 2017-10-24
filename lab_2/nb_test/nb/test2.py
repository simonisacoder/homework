#!/usr/bin/env python
import operator
from numpy import *
import sys
import math
import time
import re


def substract_data(f_name):
    f = open(f_name,'r')
    line = f.readline()
    line = f.readline()
    word_bag = []
    label_bag = []
    train_label = []
    train_text = []
    while line:
        line = line.rstrip('\n\r')
        line = re.split(',| |\n|\r',line)
        for i in range(len(line)-1):
            if line[i] not in word_bag:
                word_bag.append(line[i])
        if line[-1] not in label_bag:
            label_bag.append(line[-1])
        train_label.append(line[-1])
        line.pop()
        train_text.append(line)
        line = f.readline()

        word_tag = {}
        for i in range(len(word_bag)):
            word_tag[word_bag[i]] = i+1
    # print(train_text)
    #print(word_bag)
    #print(train_label)
    return train_text,word_bag,len(word_bag),len(train_text),train_label,label_bag,word_tag

def cal_pos(train_text,word_tag,train_label,label,row):
    # word_tag = dict()
    # label_tag = {}

    # for i in range(len(label_bag)):
    #     label_tag[word_bag[i]] = i+1
    total = 0
    sum = 0
    sum_label = 0
    num = {}
    for i in range(len(train_text)):
        total = total + len(train_text[i])
        if train_label[i] == label:
            sum_label = sum_label+1
            sum = sum+len(train_text[i])
            for j in range(len(train_text[i])):
                num[train_text[i][j]] = num.get(train_text[i][j],0)+1

    pos = []
    for i in range(col):
        pos.append(float(num.get(word_bag[i],0)+sum) / (float(total)+len(word_bag) ))
    return pos,(float(sum_label)+1)/row

def classfy(train_text,word_bag,train_label,label_bag,row,col,valid_text,word_tag):
    numer = 1.0
    demo = 0.0
    pos = []
    pos_label = []
    for i in range(len(label_bag)):
        [pos,pos_label] = cal_pos(train_text,word_bag,train_label,label_bag[i],row)
        print(label_bag[i])
        for j in range(col):
            print(word_bag[j]+':'+str(pos[j]))

    ans = 0.0
    res = []
    for h in range(len(label_bag)):
        [pos,pos_label] = cal_pos(train_text,word_bag,train_label,label_bag[i],row)
        for i in range(len(valid_text)):
            for j in range(len(valid_text[i])):
                if valid_text[i][j] in word_bag:
                    numer = numer * (pos[word_tag[valid_text[i][j]]])
                    print(numer)
            ans = pos_label*numer
            res.append([ans,label_bag[h]])
    print(res)
    #
    # or h in range(len(label_bag)):
    #     [pos,pos_label,word_tag] = cal_pos(train_text,word_bag,train_label,label_bag[i],row)
    #     for i in range(len(valid_text)):
    #         for j in range(len(valid_text[i])):
    #             for k in range(col):
    #                 if valid_text[k] in word_bag:
    #                     numer = numer * pos[word_tag[valid_text[i][k]]]




[train_text,word_bag,col,row,train_label,label_bag,word_tag] = substract_data('train_set.csv')
# [pos,pos_label] = cal_pos(train_text,word_bag,train_label,'joy',row)s
# print(pos_label)

[valid_text,valid_bag,v_col,v_row,valid_label,valid_label_bag,word_tag] = substract_data('test_set.csv')
classfy(train_text,word_bag,train_label,label_bag,row,col,valid_text,word_tag)
