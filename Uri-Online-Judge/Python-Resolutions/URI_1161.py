while True:
    try:
        soma1 = 1
        soma2 = 1
        N = input().split(" ")
        N = [int(v) for v in N]
        if N[0] != 0:
            for i in range (1, N[0]+1):
                soma1 *= i
        else:
            soma1 = 1
        if N[1] != 0:
            for i in range (1,N[1]+1):
                soma2 *= i
        else:
            soma2 = 1
        print (soma1 + soma2)
    except EOFError:
        break