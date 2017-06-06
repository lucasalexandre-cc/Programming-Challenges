N = int(input())
while N != 0:
    C = float(input())
    dias = 0
    while C > 1:
        dias += 1
        C /= 2
    print ("%i dias"%dias)
    N -= 1
