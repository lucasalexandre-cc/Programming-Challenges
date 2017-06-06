N = int(input())
um = 2
dois = 5
tres = 5
quatro = 4
cinco = 5
seis = 6
sete = 3
oito = 7
nova = 6
zero = 6
while N != 0:
    V = input()
    total = 0
    while True:
        for i in V:
            num = int(i)
            if num == 0:
                total += 6
            elif num == 1:
                total += 2
            elif num == 2:
                total += 5
            elif num == 3:
                total += 5
            elif num == 4:
                total += 4
            elif num == 5:
                total += 5
            elif num == 6:
                total += 6
            elif num == 7:
                total += 3
            elif num == 8:
                total += 7
            elif num == 9:
                total += 6
        break
    print ("%i leds"%total)
    N -= 1