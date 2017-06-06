while True:
    try:
        N = int(input())
        matriz = []
        for i in range(N):
            lista = []
            for j in range(N):
                if (j== ((N-1)-i)):
                    lista.append (2)
                elif (i==j):
                    lista.append (1)
                else:
                    lista.append (3)
            matriz.append (lista)
        for i in range (N):
            print (*matriz[i],sep="")
    except EOFError:
        break