#!/usr/bin/env python
import operator
from numpy import *
from scipy.sparse import csc_matrix
import sys
import math
import time
import re
from scipy.sparse import coo_matrix

#read the dataset and divide them into word_bag,word_list and label
def substract_word(f_name):
    f = open(f_name,'r')
    line = f.readline()
    line = f.readline()
    train_word = []
    label = []
    train_text = []
    while line:
        line = line.rstrip('\n\r')
        line = re.split(',| |\n|\r',line)
        for i in range(len(line)-1):
            if line[i] not in train_word:
                train_word.append(line[i])
        label.append(line[-1])
        line.pop()
        train_text.append(line)
        line = f.readline()
    f.close()
    # print(train_text)
    #print(train_word)
    #print(label)
    op_train_word = open('train_word','w')
    op_train_word.write(str(train_word))
    op_train_word.close()

    op_train_text = open('train_text','w')
    for i in range(len(train_text)):
        op_train_text.write(str(train_text[i])+'\n')
    op_train_text.close()

    op_train_label = open('train_label','w')
    op_train_label.write(str(label))
    op_train_label.close()

    return train_text,train_word,len(train_word),len(train_text),label

def cal_onehot(train_text,train_word,row,col):
        # f = open('/media/simon/Study/3-up/AI/lab_2/classification_dataset/train_set.csv','r')

    array = [[0 for i in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            if train_word[j] in train_text[i]:
                array[i][j] = 1
    savetxt('train_onehot',array)
    return array

#calculate the tf matrix of train_data
def cal_tf(text,word,row,col):
    tf = [[0 for i in range(col)] for i in range(row)]
    tf = array(tf).astype(float)
    d = dict()
    for i in range(row):
        sum = 0
        d.clear()
        for j in range(len(text[i])):
            d[text[i][j]] = d.get(text[i][j],0)+1
            sum = sum + 1
        for j in range(col):
            tf[i][j] = float(d.get(word[j],0))/sum
    savetxt("train_tf",tf)
    return tf

def cal_tfidf():
    tfidf = zeros_like(train_tf)
    d = {}
    for i in range(col):
        for j in range(row):
            if train_onehot[j][i] == 1:
                d[train_word[i]] = d.get(train_word[i],0) + 1
    for i in range(row):
        for j in range(col):
            tfidf[i][j] = train_tf[i][j]*math.log(float(row)/(d[train_word[j]]+1))
    return tfidf

def cal_train_data(text,word,row,col):
    onehot = loadtxt('train_onehot')
    tf = loadtxt('train_tf')
    tfidf = loadtxt('train_tfidf')
    savetxt('train_tfidf',tfidf)
    savetxt('train_onehot',onehot)
    savetxt('train_tf',tf)

def cal_valid_data(text,word,row,col,valid_text):
    valid_onehot = [[0 for i in range(col)] for i in range(row)]
    for i in range(len(valid_text)):
        for j in range(col):
            if word[j] in valid_text[i]:
                valid_onehot[i][j] = 1
    savetxt('valid_onehot',array(valid_onehot))

    tf = [[0 for i in range(col)] for i in range(len(valid_text))]
    tf = array(tf).astype(float)
    d = dict()
    for i in range(len(valid_text)):
        sum = 0
        d.clear()
        for j in range(len(valid_text[i])):
            d[valid_text[i][j]] = d.get(valid_text[i][j],0)+1
            sum = sum + 1
        for j in range(col):
            tf[i][j] = float(d.get(word[j],0))/sum
    print(tf)
    savetxt('valid_tf',array(tf))

    tfidf = zeros_like(tf)
    d = {}
    for i in range(col):
        for j in range(len(valid_text)):
            if valid_onehot[j][i] == 1:
                d[word[i]] = d.get(word[i],0) + 1
    for i in range(len(valid_text)):
        for j in range(col):
            tfidf[i][j] = tf[i][j]*math.log(float(row)/(d.get(word[j],0)+1))
    savetxt('valid_tfidf',array(tfidf))

def get_train_data():
    onehot = loadtxt('train_onehot')
    tf = loadtxt('train_tf')
    tfidf = loadtxt('train_tfidf')
    return onehot,tf,tfidf

def get_valid_data(text,word,row,col):
    onehot = loadtxt('valid_onehot')
    tf = loadtxt('valid_tf')
    tfidf = loadtxt('valid_tfidf')
    return onehot,tf,tfidf

#
# def classify0():



# train_onehot = loadtxt('/media/simon/Study/3-up/AI/lab_2/classification_dataset/train_onehot')
# global train_onehot,train_tf,train_tfidf,row,col

[train_text,train_word,col,row,train_label] = substract_word('/media/simon/Study/3-up/AI/lab_2/classification_dataset/train_set.csv')
[valid_text,valid_word,v_col,v_row,valid_label] = substract_word('validation_set.csv')

cal_train_data(train_text,train_word,row,col)
cal_valid_data(train_text,train_word,row,col,valid_text)
# train_onehot = cal_onehot(train_text,train_word,row,col)s
# train_tf = cal_tf(train_text,train_word,row,col)
# train_tfidf = cal_tfidf()

# s_train_onehot = coo_matrix(train_onehot).astype(int8)
# [train_onehot,train_tf,train_tfidf] = get_train_data()
