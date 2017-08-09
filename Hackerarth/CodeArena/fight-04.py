T = int(input())

for _ in range(T):
    inp = input().split()
    inp[0] = inp[0][::-1]
    inp[1] = inp[1][::-1]
    
    resp = int(inp[0])+int(inp[1])
    
    resp = str(resp)
    
    resp = resp[::-1]
    
    while(resp[0] == '0'):
        resp = resp[1:len(resp)]
        
    print(resp)