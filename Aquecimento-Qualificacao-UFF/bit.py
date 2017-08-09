v = int(input())
teste = 1
while(v):
    lista = []
    lista.append(v//50)
    v %= 50
    lista.append(v//10)
    v %= 10
    lista.append(v//5)
    v %= 5
    lista.append(v)
    print("Teste %i"%teste)
    print("%i %i %i %i"%(lista[0], lista[1], lista[2], lista[3]))
    print("")
    teste += 1
    v = int(input())

