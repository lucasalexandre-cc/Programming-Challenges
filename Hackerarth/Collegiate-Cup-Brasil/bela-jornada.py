x = int(input())
linha = input()
vetor = [int(v) for v in linha.split()]
 
inicial = sum(vetor)
final = 0
maximo = 0
 
for i in vetor:
    final += i
    inicial -= i
    if(final*inicial > maximo):
        maximo = final*inicial
 
print(maximo)