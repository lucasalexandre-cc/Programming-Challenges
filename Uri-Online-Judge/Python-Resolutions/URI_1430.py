C = input().split("/")
while C[0] != "*":
    lista = []
    certo = 0
    for ch in C:
        if ch != "":
            lista.append (ch)
    for x in range (len(lista)):
        tot = 0
        for y in lista[x]:
            if y == "W":
                tot +=1
            elif y == "H":
                tot += 1/2
            elif y == "Q":
                tot += 1/4
            elif y == "E":
                tot += 1/8
            elif y == "S":
                tot += 1/16
            elif y == "T":
                tot += 1/32
            elif y == "X":
                tot += 1/64
        if tot == 1:
            certo += 1
    print (certo)
    C = input().split("/")