N = int(input())
lista = []
texto = input().split(" ")
for i in range (N):
    if len(texto[i]) == 3:
        if texto[i][0] == "O" and texto[i][1] == "B":
            lista.append ("OBI")
        elif texto[i][0] == "U" and texto[i][1] == "R":
            lista.append ("URI")
        else:
            lista.append (texto[i])
    else:
        lista.append (texto[i])
print (*lista,sep=" ")
