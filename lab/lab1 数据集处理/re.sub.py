import re
# first way to check whether a word has number
def hasNum1(string):
    return any(char.isdigit() for char in string)

#second way: regular expression
def hasNum2(string)


s = "123 a:1 b:2 c:3  ab cd ef"
s = s.split()
print(s)
for i in s:
    if re.search(r'\d',s(i),flag=0):
        print(s(i).group())
    else:
        print('num')
