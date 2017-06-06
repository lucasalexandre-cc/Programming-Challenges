y = 0
while True:
    try:
        ano = int(input())
        if y != 0:
            print ("")
        y = 1
        x = 0
        if (ano %4 == 0 and ano%100!= 0) or (ano%400 == 0):
            print ("This is leap year.")
            x += 1
        if (ano%15 == 0):
            print ("This is huluculu festival year.")
            x += 1
        if ((ano %4 == 0 and ano%100!= 0) or (ano%400 == 0)) and (ano%55 == 0):
            print ("This is bulukulu festival year.")
            x += 1
        if x == 0:
            print ("This is an ordinary year.")
    except EOFError:
        break