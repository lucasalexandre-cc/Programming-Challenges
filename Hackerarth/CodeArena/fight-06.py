T = int(input())

for _ in range(T):
    s = input()
    s_aux = set(s)
    num = 0
    for i in s_aux:
        if(s.count(i)%2 != 0):
            num += 1
    if (num <= 1):
        print(0)
    else:
        print(num-1)