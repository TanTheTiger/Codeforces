t = int(input())
tot = 0
for i in range(t):
    n = int(input())
    s = list(input())
    s = [int(item) for item in s]
    for j in range(n):
        a = [item for item in s]
        a[j]  = abs(a[j]-1)
        for k in range(n):
            if a[k] == 1:
                tot += 1
    print(tot)
    tot = 0
