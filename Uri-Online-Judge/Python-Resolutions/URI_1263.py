while True:
    try:
        string = input().split(" ")
        dif = 0
        cont = 0
        for i in range(len(string)-1):
            string[i] = string[i].upper()
            string[i+1] = string[i+1].upper()
            if (string[i][0] == string[i+1][0]):
                if dif != string[i][0]:
                    cont += 1
                dif = string[i][0]
            else:
                dif = 0
        print (cont)
    except EOFError:
        break