#!/usr/bin/env python
import operator
from numpy import *
import sys
import math
import time
import re
# record the standard output


def file_write(a):
    f = open('a','w')
    sys.stdout = f

#create a class "smatrix" to save the one_hot matrix
class smatrix(object):
    #initial needs 2 argument ,row and column of the
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.num = 0
        self.data = []
    def print_data(self):
        print(self.row)
        print(self.col)
        print(self.num)
        for i in range(len(self.data)):
            print(self.data[i])

    def add(self,row,col,value):
        self.num = self.num+1
        self.data.append([row,col,value])



def substract_data():
    f = open('/media/simon/Study/3-up/AI/lab_2/classification_dataset/train_set.csv','r')
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
    return array

def get_onehot(train_word,row,col,data):
    onehot = [0 for i in range(col)]
    for i in range(col):
        if train_word[i] in data:
            onehot[i] = 1;
    return onehot

def get_tf(train_word,row,col,data):
    tf = [0 for i in range(col)]
    sum = len(data)
    d = dict()
    for i in range(sum):
        d[data[i]] = d.get(data[i],0)+1
    for i in range(col):
        tf[i] = float(d.get(train_word[i],0))/sum
    return tf

def get_idf(train_text,train_word,row,col,data):
    d = dict()
    for i in range(col):
        for j in range(row):
            if train_word[i] in train_text[j]:
                d[train_word[i]] = d.get(train_word[i],0)+1
    idf = [0 for i in range(col)]
    for i in range(col):
        idf[i] = math.log(float(row)/(d[train_word[j]]+1))
    return idf


def cal_tf(data,words,row):
    output = sys.stdout
    tf = open('tf','w')
    sys.stdout = tf

    array = [[0 for i in range(len(words))] for i in range(row)]
    d = dict()
    for i in range(row):
        sum = 0;
        string = ""
        d.clear()
        for j in range(len(data[i])):
            d[data[i][j]] = d.get(data[i][j],0)+1
            sum = sum + 1
        for j in range(len(words)):
            array[i][j] = float(d.get(words[j],0))/sum
            string = string +str(array[i][j])+' '


    tf.close()
    sys.stdout = output
    print('done2')
    return array

def cal_tf_idf(data,words,row,tf):
    output = sys.stdout
    tf_idf = open('tfidf','w')
    sys.stdout = tf_idf
    array = [[0 for i in range(len(words))] for i in range(row)]
    d = dict()
    for i in range(len(words)):
        for j in range(row):
            if words[i] in data[j]:
                d[words[i]] = d.get(words[i],0)+1

    for i in range(row):
        string = ""
        for j in range(len(words)):
            array[i][j] = tf_idf_ij = tf[i][j]*math.log(float(row)/(d[words[j]]+1))
            string = string + str(tf_idf_ij) + ' '

        string = ""

    tf_idf.close()
    sys.stdout = output
    print('done3')
    return array


#euclidean distance to classify
def classify0(inX,dataSet,labels,k,row):
    train_data = array(dataSet)
    valid_data = tile(array(inX),(row,1))
    diffMat = train_data - valid_data
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5


    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def get_valid_data(valid_data):
    f = open(valid_data,'r')
    line = f.readline()
    line = f.readline()
    label = []
    train_text = []
    while line:
        line = line.rstrip('\n\r')
        line = re.split(',| |\'|\n|\r',line)
        label.append(line[-1])
        line.pop()
        train_text.append(line)
        line = f.readline()
    # print(train_text)
    #print(train_word)
    #print(label)
    return train_text,label

def data_2_num(train_text,train_word,row,col,data):
    tf = [0 for i in range(col)]
    tf_idf = [0 for i in range(col)]
    onehot = get_onehot(train_word,row,col,data)
    tf = get_tf(train_word,row,col,data)
    idf = get_idf(train_text,train_word,row,col,data)
    for i in range(col):
        tf_idf[i] = tf[i]*idf[i]
    return onehot,tf,tf_idf

def regress0(inX,dataSet,labels,k,row):
    train_data = array(dataSet)
    valid_data = tile(array(inX),(row,1))
    diffMat = train_data - valid_data
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5

    sortedDistIndicies = distances.argsort()
    weight = array([0.0 for i in range(row)])
    for i in range(row):
        weight[i] = float(1.0/distances[i])

    struct = []
    for i in range(row):
        struct.append([distances[i],labels[i]])
    sortstruct = sorted(struct,key=lambda dis:dis[0],reverse=False)

    # weightCount = {}
    # sum = 0
    # for i in range(k):
    #     weightCount[sortstruct[i][1]] = weightCount.get(sortstruct[i][1],0) + 1.0/sortstruct[i][0]
    # for key in weightCount:
    #     sum = sum + weightCount[key]
    # for key in weightCount:
    #     weightCount[key] = weightCount[key]/sum

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def classify(train_text,train_word,row,col,label,train_data,k):
    [valid_data,answer] = get_valid_data('/media/simon/Study/3-up/AI/lab_2/classification_dataset/validation_set.csv')
    # print(valid_data,answer)
    onehot = []
    tf = []
    tf_idf = []
    for i in range(len(valid_data)):
        [a,b,c] = data_2_num(train_text,train_word,row,col,valid_data[i])
        onehot.append(a)
        tf.append(b)
        tf_idf.append(c)

    result = []
    regression = []
    for i in range(len(valid_data)):
        result.append(classify0(tf[i],train_data,label,3,row))
        regression.append(regress0(tf[i],train_data,label,3,row))
    return result,answer


def compare(answer,predict):
    cnt = 0
    for i in range(len(answer)):
        if answer[i] == predict[i]:
            cnt = cnt + 1
    return cnt


[train_text,train_word,col,row,label] = substract_data()
# print(label)
global train_onehot,train_tf,train_tfidf,valid_word,valid_label
onehot = cal_onehot(train_text,train_word,row,col)
train_tf = cal_tf(train_text,train_word,row)
train_tfidf = cal_tf_idf(train_text,train_word,row,train_tf)
[valid_word,valid_label] = get_valid_data("validation_set.csv")
for i in range(10):
    [predict,answer] = classify(train_text,train_word,row,col,label,train_tf,i)
    cnt = compare(answer,predict)    # weightCount = {}
    # sum = 0
    # for i in range(k):
    #     weightCount[sortstruct[i][1]] = weightCount.get(sortstruct[i][1],0) + 1.0/sortstruct[i][0]
    # for key in weightCount:
    #     sum = sum + weightCount[key]
    # for key in weightCount:
    #     weightCount[key] = weightCount[key]/sum
    print(cnt)

# print(len(predict))
# print(len(answer))
