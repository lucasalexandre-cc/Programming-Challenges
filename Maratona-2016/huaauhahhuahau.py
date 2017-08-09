cons = ['a', 'e', 'i', 'o', 'u']

new_inp = [x for x in input() if x in cons]

if(new_inp == new_inp[::-1]):
	print("S")
else:
	print("N")