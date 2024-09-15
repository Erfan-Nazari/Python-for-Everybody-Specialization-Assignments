# Use mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
count = 0
for line in fhandle:
    if not line.startswith("From "): continue
    count = count + 1
    print(line.split()[1])
print("There were", count, "lines in the file with From as the first word")
