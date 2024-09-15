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
    email = line.split()[1]
    counts[email] = counts.get(email,0) + 1
maxcount = None
maxemail = None
for email, count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxemail = email
print(maxemail, maxcount)
