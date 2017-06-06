def msum2(a):
	s, t= -float('infinity'), 0
	for i in range(len(a)):
		t = t + a[i]
		if t > s: s = t
		if t < 0: t= 0
	return (s)

while True:
    try:
        dia = int(input())
        custo = int(input())
        lucro = []
        for i in range(dia):
            tot = int(input())
            lucro.append(tot-custo)
        var = msum2(lucro)
        if var < 0:
            print(0)
        else:
            print(var)
    except EOFError:
        break