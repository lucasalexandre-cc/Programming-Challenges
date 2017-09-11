N = int(input())

for _ in range(N):

	num = int(input())

	nome = input().split()
	pres = input().split()

	resp = []
	for i in range(num):
		if(pres[i].count('P')/(len(pres[i])-pres[i].count('M'))) < 0.75:
			resp.append(nome[i])
	if(len(resp) == 0):
		print("")
	else:
		for i in range(len(resp)-1):
			print("%s "%resp[i], end="")
		print(resp[len(resp)-1])