name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    name = line.split()
    if len(name) > 5:
        y = name[1]
        email[y] = email.get(y,0) + 1

bigc = None
bigw = None
for w,c in email.items():
    if bigc is None or c > bigc:
        bigw = w
        bigc = c
print(bigw,bigc)
