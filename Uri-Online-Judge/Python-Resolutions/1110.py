from collections import deque

n = int(input())

while(n != 0):
	lista = deque([int (v) for v in range(n, 0, -1)])
	descartadas = []

	while True:
		aux = lista.pop()
		descartadas.append(aux)
		if len(lista) == 1:
			break
		lista.appendleft(lista.pop())
		if len(lista) == 1:
			break

	print("Discarded cards: ", end="")
	for i in range(len(descartadas)-1):
		print("%i, "%descartadas[i], end="")
	print("%i"%descartadas[len(descartadas)-1])
	
	print("Remaining card: %i"%lista[0])

	n = int(input())