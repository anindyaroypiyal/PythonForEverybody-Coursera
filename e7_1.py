# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Can't open file",fname)
    quit()
print(fh.read().upper().rstrip())
