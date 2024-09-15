count = 0
sum = 0.0
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        number = float(sval)
    except:
        print('Not a number!')
        continue
    count = count + 1
    sum = sum + number
if count == 0:
    print("No number entered!")
else:
    print('Count:', count)
    print('Sum:', sum)
    print('Average:', sum / count)