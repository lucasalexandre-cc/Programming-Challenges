inp = [int(v) for v in input().split()]
while(inp[0] != 0 or inp[1] != 0):
	A = [int(v) for v in input().split()]
	B = [int(v) for v in input().split()]

	A_set = set(A)
	B_set = set(B)

	resp_a = 0
	resp_b = 0

	for x in A_set:
		if x not in B_set:
			resp_a += 1

	for x in B_set:
		if x not in A_set:
			resp_b += 1

	print(min(resp_b, resp_a))

	inp = [int(v) for v in input().split()]