# Use mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
counts = dict()
for line in fhandle:
    if not line.startswith("From "): continue
    time = line.split()[5]
    hour = time.split(':')[0]
    counts[hour] = counts.get(hour,0) + 1
for hour,count in sorted(counts.items()):
    print(hour,count)
