N = int(input())
for i in range (N):
    d = input()
    p = 0
    cont = 0
    for j in d:
        if j == "<":
            p += 1
        elif j == ">":
            if p > 0:
                cont += 1
                p -= 1
            elif p < 0:
                p = 0
    print (cont)