def computepay(h, r):
    if 0 <= h <= 40 and r >= 0:
        return h * r
    elif h > 40 and r >= 0:
        return 40 * r + 1.5 * (h-40) * r
    else :
        print('Bad input')
        quit ()

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    hr = float(hrs)
    rt = float(rate)
except:
    print('Bad input')
    quit ()
p = computepay(hr, rt)
print("Pay", p)