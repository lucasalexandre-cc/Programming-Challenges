def maiorAB(vetor):
    soma, aux = -float('infinity'), 0
    ini = 0
    fim = 0
    ini_aux = 0
    for i in range(len(vetor)):
        aux += vetor[i]
        if(aux > soma):
            fim = i
            ini = ini_aux
            soma = aux
        elif(aux == soma):
            if(i - ini_aux > fim - ini):
                fim = i
                ini = ini_aux
        if(aux < 0):
            ini_aux = i+1
            aux = 0
    return ini, fim, soma

n = int(input())
teste = 1
while(n):
    lista = []
    for i in range(n):
        x = [int (z) for z in input().split(" ")]
        lista.append(x[0] - x[1])
    A, B, soma = maiorAB(lista)
    print("Teste %i"%teste)
    if soma <= 0:
        print("nenhum")
    else:
        print("%i %i"%(A+1, B+1))
    print("")
    teste += 1
    n = int(input())