N = int(input())
while N != 0:
    lista = []
    lista1 = []
    total = 1
    frase = input()
    for i in frase:
        if i != " " and i != ",":
            lista.append(i)
    lista1.append (lista[0])
    for i in lista:
        cond = 0
        for j in range (len(lista1)):
            if i == lista1[j]:
                cond += 1
        if cond == 0:
            total += 1
            lista1.append (i)
    if total == 26:
        print ("frase completa")
    elif total >= 13 and total < 26:
        print ("frase quase completa")
    else:
        print ("frase mal elaborada")
    N -= 1