N = int(input())

for i in range (N):
    resp = 0
    X = input().split(" ")
    X = [int(v) for v in X]
    while X[1] != 0:
        if X[0]%2 == 0:
            X[0] += 1
        resp += X[0]
        X[0] += 2
        X[1] -= 1
    print (resp)