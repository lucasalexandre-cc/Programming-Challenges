ano = 0
mes = 0
dia = 0

dias = int(input())

while dias != 0:
    if dias >= 365:
        ano += 1
        dias -= 365
    elif dias < 365 and dias >= 30:
        mes += 1
        dias -= 30
    elif dias < 30:
        dia += 1
        dias -= 1
print ("%i ano(s)"%ano)
print ("%i mes(es)"%mes)
print ("%i dia(s)"%dia)