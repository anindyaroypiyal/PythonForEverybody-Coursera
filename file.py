#x = input('enter file name:')
try:
    f = open("box.txt" , "r")
except:
    print('file not found')
    quit()
for line in f:
    print(line)
