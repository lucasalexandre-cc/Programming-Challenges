N = int(input())
while N != 0:
    total_grao = 0
    X = int(input())
    for i in range (X):
        total_grao += 2**i
    kg = int((total_grao/12)/1000)
    N -= 1
    print ("%i kg"%kg)