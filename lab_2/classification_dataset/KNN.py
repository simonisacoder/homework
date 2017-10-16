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
    word_list = []
    label = []
    data_list = []
    while line:
        line = line.rstrip('\n\r')
        line = re.split(',| |\n|\r',line)
        for i in range(len(line)-1):
            if line[i] not in word_list:
                word_list.append(line[i])
        label.append(line[-1])
        line.pop()
        data_list.append(line)
        line = f.readline()
    # print(data_list)
    #print(word_list)
    #print(label)
    return data_list,word_list,len(word_list),len(data_list),label

def cal_onehot(data_list,word_list,row,col):
        # f = open('/media/simon/Study/3-up/AI/lab_2/classification_dataset/train_set.csv','r')

    array = [[0 for i in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            if word_list[j] in data_list[i]:
                array[i][j] = 1
    return array

def get_onehot(word_list,row,col,data):
    onehot = [0 for i in range(col)]
    for i in range(col):
        if word_list[i] in data:
            onehot[i] = 1;
    return onehot

def get_tf(word_list,row,col,data):
    tf = [0 for i in range(col)]
    sum = len(data)
    d = dict()
    for i in range(sum):
        d[data[i]] = d.get(data[i],0)+1
    for i in range(col):
        tf[i] = float(d.get(word_list[i],0))/sum
    return tf

def get_idf(data_list,word_list,row,col,data):
    d = dict()
    for i in range(col):
        for j in range(row):
            if word_list[i] in data_list[j]:
                d[word_list[i]] = d.get(word_list[i],0)+1
    idf = [0 for i in range(col)]
    for i in range(col):
        idf[i] = math.log(float(row)/(d[word_list[j]]+1))
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
        print(string)

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
        print(string)
        string = ""

    tf_idf.close()
    sys.stdout = output
    print('done3')
    return array


#euclidean distance to classify
def classify0(inX,dataSet,labels,k,row):
    dataSetSize = row
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
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


def get_test_data(test_data):
    f = open(test_data,'r')
    line = f.readline()
    line = f.readline()
    label = []
    data_list = []
    while line:
        line = line.rstrip('\n\r')
        line = re.split(',| |\'|\n|\r',line)
        label.append(line[-1])
        label.pop()
        data_list.append(line)
        line = f.readline()
    # print(data_list)
    #print(word_list)
    #print(label)
    return data_list,label

def data_2_num(data_list,word_list,row,col,data):
    tf = [0 for i in range(col)]
    tf_idf = [0 for i in range(col)]
    onehot = get_onehot(word_list,row,col,data)
    tf = get_tf(word_list,row,col,data)
    idf = get_idf(data_list,word_list,row,col,data)
    for i in range(col):
        tf_idf[i] = tf[i]*idf[i]
    return onehot,tf,tf_idf

def classify(data_list,word_list,row,col,label):
    [test_data,answer] = get_test_data('test_data')
    onehot = []
    tf = []
    tf_idf = []
    for i in range(len(test_data)):
        [a,b,c] = data_2_num(data_list,word_list,row,col,test_data[i])
        onehot.append(a)
        tf.append(b)
        tf_idf.append(c)

    result = []
    for i in range(len(test_data)):
        result.append(classify0(data_list,word_list,row,col,tf[i]))
    return result





[data_list,word_list,col,row,label] = substract_data()
one_hot = cal_onehot(data_list,word_list,row,col)
tf = cal_tf(data_list,word_list,row)
tf_idf = cal_tf_idf(data_list,word_list,row,tf)
predict = classify(data_list,word_list,row,col,label)
print(predict)

# [test_data,answer] = get_test_data("validation_set.csv")
