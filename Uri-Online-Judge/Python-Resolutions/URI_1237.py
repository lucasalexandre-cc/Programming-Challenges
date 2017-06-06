while True:
    try:
        s1 = input()
        s2 = input()
        seq = 0
        lista = ""
        seq = 0
        for i in range(len(s1)):
            lista+= s1[i]
            x = i
            if lista in s2:
                x+= 1
                while lista in s2 and x <= len(s1)-1:
                    lista+= s1[x]
                    x += 1
                if lista in s2:
                    if len(lista) > seq:
                        seq = len(lista)
                else:
                    if len(lista)-1 > seq:
                        seq = len(lista)-1
            lista = ""
        print(seq)
    except EOFError:
        break