from math import sqrt, ceil
from collections import deque

def divisores(C):
	d1 = deque()
	d2 = deque()

	for i in range(1, ceil(sqrt(C))+1):
		if C%i == 0:
			d1.append(i)
			d2.appendleft(C//i)
	return list(d1) + list(d2)

A, B, C, D = map(int, input().split())

div = divisores(C)

achou = -1
for i in div:
	if (i%A == 0 and i%B != 0 and D%i != 0):
		achou = 1
		print(i)
		break
if (achou == -1):
	print(achou)