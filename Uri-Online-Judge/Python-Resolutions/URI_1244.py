def por_tamanho(x):
    return (len(x))
N = int(input())
for i in range (N):
    x = input().split(" ")
    x.reverse ()
    x = sorted (x,key=por_tamanho)
    x.reverse ()
    print (*x,sep=" ")
