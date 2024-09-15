import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_1870298.txt"
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
total = 0
integers = re.findall('[0-9]+', fhandle.read())
if len(integers) != 0: 
    for snum in integers:
        total = total + int(snum)
print(total)