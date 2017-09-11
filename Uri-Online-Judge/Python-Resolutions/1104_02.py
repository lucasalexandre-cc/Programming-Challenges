inp = [int(v) for v in input().split()]
while(inp[0] != 0 or inp[1] != 0):
	A = [int(v) for v in input().split()]
	B = [int(v) for v in input().split()]

	A_set = set(A)
	B_set = set(B)
	set_Final = set(list(A_set)+list(B_set))

	print(min(len(set_Final)-len(A_set), len(set_Final)-len(B_set)))

	inp = [int(v) for v in input().split()]