def ordenando(vetor, ini, fim):
    impar = []
    par = []
    for i in range(ini, fim):
        if vetor[i][1]%2 == 0:
            par.append([vetor[i][1], vetor[i][0]])
        else:
            impar.append([vetor[i][1], vetor[i][0]])
    impar.sort()
    impar.reverse()
    par.sort()

    index_impar = 0
    index_par = 0
    for i in range(ini, fim):
        if index_impar < len(impar):
            vetor[i][0] = impar[index_impar][1]
            vetor[i][1] = impar[index_impar][0]
            index_impar += 1
        else:
            vetor[i][0] = par[index_par][1]
            vetor[i][1] = par[index_par][0]
            index_par += 1

x = [int (v) for v in input().split()]
while(x[0] != 0 and x[1] != 0):
    inp = []
    for i in range(x[0]):
        num = int(input())
        if num < 0:
            num = num*-1
            inp.append([num%x[1] * -1, num*-1])
        else:
            inp.append([num % x[1], num])
    inp.sort()
    ini = 0
    fim = 0
    for i in range(len(inp)-1):
        if fim <= i and inp[i][0] == inp[i+1][0]:
            ini = i
            fim = i+1
            valor = inp[i][0]
            while(fim < len(inp) and inp[fim][0] == valor):
                fim += 1
            ordenando(inp, ini, fim)

    print("%i %i" % (x[0], x[1]))
    for i in range(x[0]):
        print(inp[i][1])
    x = [int(v) for v in input().split()]
print("%i %i" % (0, 0))