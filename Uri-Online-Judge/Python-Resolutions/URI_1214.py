C = int(input())
while C != 0:
    Total = 0
    N = input().split(" ")
    N = [int(v) for v in N]
    media = (sum(N)-N[0])/(len(N)-1)
    for i in range (1,len(N)):
        if N[i] > media:
            Total += 1
    Total /= N[0]
    Total *= 100
    print ("%.3f%%"%Total)
    C -= 1