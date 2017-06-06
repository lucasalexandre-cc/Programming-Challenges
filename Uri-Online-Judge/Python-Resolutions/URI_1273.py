N = int(input())
while N != 0:
    maxi = 0
    lista = []
    for i in range (N):
        P = input()
        lista.append (P)
        if len(P) > maxi:
            maxi = len(P)
    for i in range (len(lista)):
        while len(lista[i]) != maxi:
            lista[i] = (" ")+lista[i]
        print (lista[i])
    N = int(input())
    if N != 0:
        print ("")