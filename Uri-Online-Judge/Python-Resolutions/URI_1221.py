from math import sqrt
N = int(input())
for i in range(N):
    num = int(input())
    if num%2 == 0:
        if num != 2:
            print("Not Prime")
        else:
            print("Prime")
    else:
        cont = 0
        for j in range(1, int(sqrt(num)),2):
            if num%j == 0:
                cont += 1
        if cont > 1:
            print ("Not Prime")
        else:
            print ("Prime")