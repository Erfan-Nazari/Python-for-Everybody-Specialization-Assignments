# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
count = None
total = None
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = float(line[line.find(':') + 1 :].strip())
    if count is None:
        count = 1
        total = num
    else:
        count = count + 1
        total = total + num
if count is None:
    print("No spam confidence line found.")
else:
    print("Average spam confidence:", total / count)