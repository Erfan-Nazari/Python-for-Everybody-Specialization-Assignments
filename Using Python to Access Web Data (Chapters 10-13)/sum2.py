import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_1870298.txt"
try:
    fhandle = open(fname)
except:
    print('File cannot open:', fname)
    quit()
print(sum([int(num) for num in re.findall('[0-9]+', fhandle.read())]))