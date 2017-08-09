import math

def phi(n):
    total = 0
    
    for i in range(1, n+1):
        if math.gcd(n, i) == 1:
            total += 1

    return total

T = int(input())
for _ in range(T):
    N = int(input())
    tot = 0
    for i in range(1, N+1):
        tot += phi(i)
    print(tot)