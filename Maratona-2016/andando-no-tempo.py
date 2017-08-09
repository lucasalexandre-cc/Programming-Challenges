inp = [int(v) for v in input().split()]

if(inp[0] == inp[1] or inp[0] == inp[2] or inp[1] == inp[2] or inp[0] == inp[1]+inp[2] or inp[1] == inp[0]+inp[2] or inp[2] == inp[0]+inp[1]):
	print('S')
else:
	print('N')