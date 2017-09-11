def dijkstra_path(grafo, origem, fim): #retorna a menor distancia de um No origem até um No destino e o caminho até ele

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice) #inclui os vertices nos não visitados    
        distanciaAtual[vertice] = float('inf') #inicia os vertices como infinito

    distanciaAtual[atual] = [0,origem] 

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                 distanciaAtual[vizinho] = [pesoCalc,atual]
                 controle[vizinho] = pesoCalc
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1]) #seleciona o menor vizinho
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]
    if(distanciaAtual[fim] == float("inf")):
      return None
    else:
      return distanciaAtual[fim][0]  

def criandoGrafo(N):
	dic = {}
	for i in range(1, N+1):
		dic[i] = {}
	return dic

def zerandoValores(grafo):
	for i in grafo.keys():	#Keys da 'origem'
		for j in grafo[i].keys(): 	#Keys do destino da origem
			vetor = grafo[j].keys()
			if i in vetor:
				grafo[j][i] = 0
				grafo[i][j] = 0
	return grafo

cont = 0
N, E = [int(v) for v in input().split()]
while(N!= 0 or E != 0):
	if cont != 0:
		print("")
	dic = criandoGrafo(N)
	for _ in range(E):
		x, y, z = [int(v) for v in input().split()]
		dic[x][y] = z	
	dic = zerandoValores(dic)
	k = int(input())
	for _ in range(k):
		x, y = [int(v) for v in input().split()]
		resp = dijkstra_path(dic, x, y)
		if(resp == None):
			print("Nao e possivel entregar a carta")
		else:
			print(resp)
	cont += 1
	N, E = [int(v) for v in input().split()]