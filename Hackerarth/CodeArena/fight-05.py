T = int(input())

for _ in range(T):
    inp = [int(v) for v in input().split()]
    A = [inp[0], inp[1]]
    B = []
    for i in range(2, 2+inp[3]):
        A.append((A[i-1]+A[i-2])%inp[3])
    
    A_aux = set(A)
    tot = 0
    for i in A_aux:
        tot += A.count(i)**2
    print(tot)