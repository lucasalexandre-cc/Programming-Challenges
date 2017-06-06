frase = input()
while frase != '*':
    frase = frase.upper()
    frase = frase.split(" ")
    p = frase[0][0]
    cont = 0
    while True:
        if frase[cont][0] != p:
            print('N')
            break
        cont += 1
        if cont == len(frase):
            print('Y')
            break
    frase = input()
