dic = {
	'A': [0, 1],
	'B': [2, 3],
	'C': [4, 5],
	'D': [6, 7],
	'E': [8, 9]
}

def apareceMais(vetor):
	vetor_aux = set(vetor)
	maxx = 0
	resp = 0
	for i in vetor_aux:
		aux = vetor.count(i)
		if aux > maxx:
			resp = i
			maxx = aux
	return resp

cont = 1
N = int(input())
while(N != 0):
	lista = [[], [], [], [], [], []]
	for _ in range(N):
		inp = [x for x in input().split()]
		letras = inp[10:17]
		i = 0
		for j in range(6):
			lista[i].append(inp[dic[letras[j]][0]])
			lista[i].append(inp[dic[letras[j]][1]])
			i += 1
	print("Teste %i"%cont)
	print("%s %s %s %s %s %s "%(apareceMais(lista[0]), apareceMais(lista[1]), apareceMais(lista[2]), apareceMais(lista[3]), apareceMais(lista[4]), apareceMais(lista[5])))
	print("")
	cont += 1
	N = int(input())