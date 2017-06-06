def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
num = input()
while num != '0':
    total = 0
    for i in range(len(num),0,-1):
        total += (int(num[len(num)-i])*fatorial(i))
    print (total)
    num = input()