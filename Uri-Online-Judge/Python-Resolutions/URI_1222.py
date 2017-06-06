while True:
    try:
        N = input().split(" ")
        N = [int(v) for v in N]
        texto = input().split(" ")
        lin = 0
        linha = 0
        for i in range(N[0]):
            linha += len(texto[i])
            if linha > N[2]:
                lin += 1
                linha = len(texto[i])
            if i != N[0]-1:
                linha += 1
                if linha > N[2]:
                    lin += 1
                    linha = 0
        lin += 1
        pag = lin/N[1]
        if pag%1 != 0:
            pag = int(pag) + 1
        print (int(pag))
    except EOFError:
        break