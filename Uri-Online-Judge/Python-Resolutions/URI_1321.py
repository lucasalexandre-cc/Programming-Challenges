num = input().split(" ")
num = [int(v) for v in num]
while sum(num) != 0:
    princesa = [num[0],num[1],num[2]]
    principe = [num[3],num[4]]
    cont_final = []
    for i in principe:
        cont = 0
        for j in princesa:
            if i>j:
                cont += 1
        cont_final.append(cont)
    valor = 0
    cont_final.sort()
    princesa.sort()
    if (cont_final[0] == 2 and cont_final[1]==2)or(cont_final[0] == 2 and cont_final[1]==3):
        valor = princesa[1]+1
    elif (cont_final[0] == 0 and cont_final[1] == 3) or (cont_final[0]==1 and cont_final[1]==3):
        valor = princesa[2]+1
    elif cont_final[0] == 3 and cont_final[1] == 3:
        valor = 1
    else:
        valor = 0

    if valor == 0:
        print(-1)
    else:
        while valor in princesa or valor in  principe:
            valor += 1
        if valor <= 52 and valor > 0:
            print(valor)
        else:
            print(-1)
    num = input().split(" ")
    num = [int(v) for v in num]