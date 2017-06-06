N = int(input())
while N != 0:
    soma = 0
    for i in range (N,0,-1):
        soma += 1*(i*i)
    print (soma)
    N = int(input())