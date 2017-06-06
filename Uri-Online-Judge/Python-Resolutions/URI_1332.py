N = int(input())
while N != 0:
    one1 = two1 = 0
    palavra = input()
    if len(palavra) == 3:
        if palavra[0] == "o":
            one1 += 1
        elif palavra[0] == "t":
            two1 += 1
        if palavra[1] == "n":
            one1 += 1
        elif palavra[1] == "w":
            two1 += 1
        if palavra[2] == "e":
            one1 += 1
        elif palavra[2] == "o":
            two1 += 1
        if one1 > two1:
            print (1)
        else:
            print (2)
    else:
        print (3)
    N -= 1