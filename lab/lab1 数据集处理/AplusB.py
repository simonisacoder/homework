#!/usr/bin/env python
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

def printf(matrix):
    for i in range(3):
        print(matrix[i])
    for i in range(len(matrix)-3):
        print(matrix[3+i])

a = [5,5,3,[1,2,2],[2,2,3],[5,3,5]]
b = [5,5,2,[2,2,2],[5,1,1]]
printf(a)
printf(b)
printf(plus(a,b))
