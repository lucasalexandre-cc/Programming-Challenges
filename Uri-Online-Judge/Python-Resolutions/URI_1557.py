N = int(input())
while N != 0:
    maior_n = len(str((2**(N-1))**2))
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            test = str(1*2**(i+j))
            linha.append(test.rjust(maior_n))
        matriz.append(linha)
    for i in range(N):
        print (*matriz[i],sep =" ")
    print ("")
    N = int(input())