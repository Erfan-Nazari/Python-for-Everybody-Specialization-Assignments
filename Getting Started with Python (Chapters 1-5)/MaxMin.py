max = None
min = None
while True :
    sval = input("Enter an integer: ")
    if sval == "done" :
        break
    try:
        number = int(sval)
    except:
        print('Invalid input')
        continue
    if max is None:
        max = number
        min = number
    elif number > max:
        max = number
    elif number < min:
        min = number
if max is None:
    print("No number entered!")
else:
    print('Maximum is', max)
    print('Minimum is', min)