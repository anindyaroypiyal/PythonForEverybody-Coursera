import re
x = input('Enter file name: ')
han = open(x)
li = list()
i = 0
for line in han:
    num = re.findall('[0-9]+',line)
    if len(num) != 0:
        for nu in num:
            li.append(int(num[i]))
            i+=1
            if i >= len(num):
                i = 0
print('sum = ',sum(li))
