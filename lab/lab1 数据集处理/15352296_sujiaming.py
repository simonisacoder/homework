#!/usr/bin/env python
import re
import sys
import math
import time
#ai
def hasNum1(string):
    return any(char.isdigit() for char in string)

def hasNum2(string):
    return bool(re.search(r'\d',string))

def substract_data():
    f = open('semeval','r')
    line = f.readline()
    data_list = []
    while line:
        line = line.split()
        tmp = []
        for i in range(len(line)):
            if not hasNum2(line[i]):
                tmp.append(line[i])
        data_list.append(tmp)
        line = f.readline()
        words = []
        for i in range(len(data_list)):
            for j in range(len(data_list[i])):
                if data_list[i][j] not in words:
                    words.append(data_list[i][j])
    f.close()
    # print(data_list)
    return data_list,words,len(data_list)

def cal_one_hot(data,words,row):
    output = sys.stdout
    one_hot = open('onehot','w')
    sys.stdout = one_hot
    result = []
    array = [[0 for i in range(len(words))] for i in range(row)]
    for i in range(row):
        string = ""
        for j in range(len(words)):
            if words[j] in data[i]:
                array[i][j] = 1
                string = string + "1 "
            else:
                string = string + "0 "
        result.append(string)
            # print(string)
    for i in range(len(result)):
        print(result[i])

    sys.stdout = output
    one_hot.close()
    print('done1')
    return array

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

    d = dict()
    for i in range(len(words)):
        for j in range(row):
            if words[i] in data[j]:
                d[words[i]] = d.get(words[i],0)+1

    for i in range(row):
        string = ""
        for j in range(len(words)):
            tf_idf_ij = tf[i][j]*math.log(float(row)/d[words[j]])/math.log(2)
            string = string + str(tf_idf_ij) + ' '
        print(string)
        string = ""

    tf_idf.close()
    sys.stdout = output
    print('done3')

def onehot_to_smatrix(onehot,row,col):
    output = sys.stdout
    smatrix = open('smatrix','w')
    sys.stdout = smatrix

    result = [];
    result.append(row)
    result.append(col)
    result.append(0)

    num = 0
    for i in range(row):
        for j in range(col):
            if not onehot[i][j] == 0:
                result.append([1,i,j])
                num = num + 1
    result[2] = num

    for i in range(3):
        print(result[i])
    for i in range(result[2]):
        print(result[3+i])

    smatrix.close()
    sys.stdout = output

def plus(a,b):
    c = a
    for i in range(b[2]):
        flag = False
        for j in range(a[2]):
            if a[3+j][1] == b[3+i][1] and a[3+j][2] == b[3+i][2]:
                c[3+j][0] = a[3+j][0] + b[3+i][0]
                flag = True
        if not flag:
            c.append([b[i+3][0],b[i+3][1],b[i+3][2]])
            c[2] = c[2]+1
    c_part = sorted(c[3:len(c)],key=lambda x:(x[1],x[2]))
    c[3:len(c)] = c_part
    return c    


def main():
    [data,words,row] = substract_data()
    start_time = time.clock()
    one_hot_matrix = cal_one_hot(data,words,row)
    tf_matrix = cal_tf(data,words,row)
    cal_tf_idf(data,words,row,tf_matrix)
    onehot_to_smatrix(one_hot_matrix,row,len(words))
    end_time = time.clock()
    print(end_time-start_time)
main()
