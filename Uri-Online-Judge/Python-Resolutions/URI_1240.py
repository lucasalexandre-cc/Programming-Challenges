N = int(input())
while N != 0:
    AB = input().split(" ")
    AB = [eval(v) for v in AB]
    a = AB[1]
    alg = 0
    while a != 0:
        a //=10
        alg += 1
    if(AB[0]%(10**alg)) == AB[1]:
        print ("encaixa")
    else:
        print ("nao encaixa")
    N -= 1