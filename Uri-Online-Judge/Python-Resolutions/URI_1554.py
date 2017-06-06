C = int(input())
for z in range (C):
    N = int(input())
    branca = input().split(" ")
    branca = [int(v) for v in branca]
    cord = input().split(" ")
    cord = [int(v) for v in cord]
    d = ((branca[0]-cord[0])**2 + (branca[1]-cord[1])**2)*(1/2)
    pos_d = 1
    for i in range(1,N):
        cord = input().split(" ")
        cord = [int(v) for v in cord]
        d1 = ((branca[0]-cord[0])**2 + (branca[1]-cord[1])**2)*(1/2)
        if d1 < d:
            d = ((branca[0]-cord[0])**2 + (branca[1]-cord[1])**2)*(1/2)
            pos_d = i+1
    print (pos_d)
