# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count+=1
    num = line.find(':')
    a = float(line[num+1:].strip())
    s = s + a
print("Average spam confidence:",s/count)
