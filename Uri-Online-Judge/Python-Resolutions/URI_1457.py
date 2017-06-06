T = int(input())
for z in range(T):
    num  = input().split("!")
    num2 = len(num)-1
    num = int(num[0])
    total = num
    num3 = num2
    while num-num2 >= 1:
        total *= (num-num2)
        num2 += num3
    print(total)