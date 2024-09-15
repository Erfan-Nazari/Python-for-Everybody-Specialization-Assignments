# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
for line in fhandle:
    line = line.rstrip()
    line = line.upper()
    print(line)