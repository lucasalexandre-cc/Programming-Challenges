def balanceado(vet):
    vet.sort()
    return vet[(len(vet)//2)]
 
in1 = [int(v) for v in input().split(" ")]
vetor = [int(v) for v in input().split(" ")]
 
vetor_aux = []
for i in range(in1[1]):
    vetor_aux.append(vetor[i])
maximo = balanceado(vetor_aux.copy())
 
for i in range(in1[1], in1[0]):
    vetor_aux.remove(vetor_aux[0])
    vetor_aux.append(vetor[i])
    x = balanceado(vetor_aux.copy())
   
    if x>maximo:
        maximo = x
 
print(maximo)