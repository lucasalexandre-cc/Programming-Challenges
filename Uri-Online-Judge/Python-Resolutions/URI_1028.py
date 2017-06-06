N = int(input())
for x in range (N):
    Y = input().split(" ")
    Y = [int(v)for v in Y]
    resto = 1
    while resto != 0:
        resto = Y[0]%Y[1]
        Y[0] = Y[1]
        Y[1] = resto
    print (Y[0])