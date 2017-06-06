N = int(input())
for z in range(N):
    cont = 0
    M = int(input())
    P = input().split(" ")
    P = [int(v) for v in P]
    P_aux = P.copy()
    P_aux.sort()
    P_aux.reverse()
    for i in range(M):
        if P[i] == P_aux[i]:
            cont += 1
    print (cont)