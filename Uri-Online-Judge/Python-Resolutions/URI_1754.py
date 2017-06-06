T = int(input())
for i in range(T):
    X = input().split(" ")
    X = [int(v)for v in X]
    K = X[0]//X[1]
    if X[0] < X[1]:
        K = 2
    elif not( X[0]//X[1] == X[0]/X[1]):
        K += 1
    print (K)
