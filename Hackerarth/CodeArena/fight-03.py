T = int(input())

for _ in range(T):
    inp = [int (v) for v in input().split()]
    
    val = inp[1] - inp[0]
    if(val < inp[2]):
        print(val//inp[2])