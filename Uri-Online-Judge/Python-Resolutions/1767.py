n = int(input())

for _ in range(n):
	pac = int(input())

	lista= []
	for _ in range(pac):
		inp = [int(v) for v in input().split()]
		lista.append([inp[1]/inp[0], inp[0], inp[1]])
	lista.sort()

	brinquedos = 0
	peso = 0
	pac_sobrando = pac
	for i in range(pac):
		if(lista[i][2]+peso <= 50):
			peso += lista[i][2]
			brinquedos += lista[i][1]
			pac_sobrando -= 1
	print(lista)
	print("%i brinquedos"%(brinquedos))
	print("Peso: %i kg"%(peso))
	print("sobra(m) %i pacote(s)"%(pac_sobrando))
	print("")
