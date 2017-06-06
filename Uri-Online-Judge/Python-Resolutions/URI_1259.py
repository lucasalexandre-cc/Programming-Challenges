x = int(input())
lista_impar = []
lista_par = []
for i in range(x):
    num = int(input())
    if num%2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
lista_par.sort()
lista_impar.sort()
for i in lista_par:
    print(i)
for i in range(len(lista_impar)-1,-1,-1):
    print(lista_impar[i])