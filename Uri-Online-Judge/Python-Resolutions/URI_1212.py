valor = input().split(" ")
valor = [int(v) for v in valor]
while valor[0] != 0 or valor[1] != 0:
    carry = 0
    arm = 0
    while True:
        sum = valor[0]%10 + valor[1]%10 + arm
        arm = 0
        valor[0] //= 10
        valor[1] //=10
        if sum >= 10:
            carry += 1
            if arm == 10:
                arm = 1
            else:
                arm += 1
        if valor[0] == 0 and valor[1] == 0:
            break
    if carry == 0:
        print ("No carry operation.")
    elif carry == 1:
        print ("1 carry operation.")
    else:
        print ("%i carry operations."%carry)
    valor = input().split(" ")
    valor = [int(v) for v in valor]