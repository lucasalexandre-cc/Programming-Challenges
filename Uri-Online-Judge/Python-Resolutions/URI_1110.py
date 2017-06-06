v = int(input())
while v != 0:
    lista = []
    for i in range(v,0,-1):
        lista.append(i)
    passo = 0
    descartada = []
    while len(lista) > 1:
        lista2 = []
        for i in range(len(lista)-1,-1,-1):
            if passo == 0:
                descartada.append(lista[i])
                passo = 1
            elif passo == 1:
                lista2.append(lista[i])
                passo = 0
        lista = lista2
        lista.reverse()
    print('Discarded cards:',end=' ')
    print(*descartada,sep = ", ")
    print('Remaining card: %i'%lista[0])
    v = int(input())