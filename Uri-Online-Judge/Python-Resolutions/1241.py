x = int(input())
for _ in range(x):
    inp = input().split()
    len_A = len(inp[0])
    len_B = len(inp[1])
    if (len_B > len_A):
        print("nao encaixa")
    elif inp[0] == inp[1]:
        print("encaixa")
    else:
        cond = True
        index = 0
        for i in range(len_A - len_B, len_A):
            if inp[0][i] != inp[1][index]:
                cond = False
                break
            index += 1

        if cond:
            print("encaixa")
        else:
            print("nao encaixa")