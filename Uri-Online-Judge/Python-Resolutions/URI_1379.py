num = input().split(" ")
num = [int(v) for v in num]
while num[0] != 0 or num[1] != 0:
    num.sort()
    num3 = 2*num[0]-num[1]
    print(num3)
    num = input().split(" ")
    num = [int(v) for v in num]