N = int(input())
while N != 0:
    C = input().split(" ")

    palavra = ""
    for i in C:
        if i != "":
            palavra += i[0]
    print(palavra)
    N -= 1
