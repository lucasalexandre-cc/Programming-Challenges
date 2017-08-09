N = int(input())
A = [int (v) for v in input().split()]
Q = int(input())
for _ in range(Q):
    Q_atual = [int (v) for v in input().split()]
    if Q_atual[0] == 0:
        A[Q_atual[1]-1] = Q_atual[2]
    else:
        B = []
        for i in range(N):
            B.append(1)
            for j in range(N):
                if(i != j):
                    B[i] = B[i]*A[j]
        print(B[Q_atual[1]-1]%1000000007)