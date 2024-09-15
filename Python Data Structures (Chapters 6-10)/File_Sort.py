# Use romeo.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "romeo.txt"
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
lst = list()
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)