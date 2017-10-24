
f = open('KNN.py','r')
g = open('knn0.py','w')

line = f.readline()
while line:
    line.replace('data_list','train_text')
    g.write(line)
    print(line)
    line = f.readline()

f.close()
g.close()
