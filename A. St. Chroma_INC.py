t = int(input())
for i in range(t):
    n = input().split(' ')
    x = int(n[1])
    n = int(n[0])
    o = []
    if n>x:
        for j in range(x):
            o.append(j)
        for j in range(n-1,n-x-1,-1):
            o.append(j)
    elif n<=x:
        for j in range(n):
            o.append(j)
    print(o)


            
            