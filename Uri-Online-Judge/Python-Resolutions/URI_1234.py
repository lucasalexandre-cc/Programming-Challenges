while True:
    try:
        texto = input()
        lista = []
        vari = 1
        for i in range (len(texto)):
            if texto[i] == " ":
                lista.append (" ")
            else:
                if vari%2 == 1:
                    lista.append(texto[i].upper())
                    vari += 1
                else:
                    lista.append (texto[i].lower())
                    vari += 1
        print (*lista,sep="")
    except EOFError:
        break