score = input("Enter Score: ")
try:
    s = float(score)
except:
    print('Bad input')
    quit ()
if 0 <= s <= 1:
    if s >= 0.9:
        g = 'A'
    elif s >= 0.8:
        g = 'B'
    elif s >= 0.7:
        g = 'C'
    elif s >= 0.6:
        g = 'D'
    else :
        g = 'F'
else :
    print('Bad input')
    quit ()
print('Grade:', g)