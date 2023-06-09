name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
    if not line.startswith('From'):
        continue
    x = line.split()
    if len(x) > 5:
        a = x[5].split(':')
        dic[a[0]] = dic.get(a[0],0) + 1

lst = list()
for k,v in dic.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print(k,v)
