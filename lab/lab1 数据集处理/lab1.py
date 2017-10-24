#!/usr/bin/env python
import re
import sys
def hasNum1(string):
    return any(char.isdigit() for char in string)

def hasNum2(string):
    return bool(re.search(r'\d',string))


output = sys.stdout
one_hot = open('one_hot','w')
sys.stdout = one_hot

f = open('semeval','r')

words = []
line = f.readline()
while line:
    line = line.split()
    for i in range(len(line)):
        if not hasNum2(line[i]) and line[i] not in words:
            words.append(line[i])
    line = f.readline()


f.close()
f = open('semeval','r')

line = f.readline()
w_len = len(words)
tmp = list()
cnt = 1
row = str(cnt) + ":"
while line:
    line = line.split()
    for j in range(len(line)):
        if not hasNum2(line[j]):
            tmp.append(line[j])
    for j in range(w_len):
        # for k in range(len(line)):
        #     if not hasNum2(line[k]):
        #         d[line[k]] = d.get(line[k],default=0)+1
        if words[j] in tmp:
            row = row + "1 "
        else:
            row = row + "0 "
    print(row)
    row = str(cnt) + ":"
    tmp = []
    cnt = cnt + 1;
    line = f.readline()
    f.close()
    one_hot.close()

tf = open('tf','w')
sys.stdout = tf

f = open("semeval","r")
line = f.readline()
d = dict()
sum = 0
row = ""
while line:
    line = line.split()
    sum = 0
    for i in range(len(line)):
        if not hasNum2(line[i]):
            d[line[i]] = d.get(line[i],0)+1
            sum = sum + 1
    print(sum)
    for i in range(w_len):
        # print(d.get(words[i],0))
        row = row + str(float(d.get(words[i],0))/sum) + " "
    print(row)
    line = f.readline()
    row = ""
    d = dict()
f.close()
sys.stdout = output

# 1246*2749

idf = [[0 for i in range(2749)] for i in range(1246)]
f = open("semeval","r")
lines = f.readlines()
for i in range
    for i in range()
    # print(idf)
    # print(len(words))
    # f = open('semeval','r')
    # num_row = f.readlines()
    # print(len(num_row))
    print("done")
