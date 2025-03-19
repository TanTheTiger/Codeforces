n = int(input())
t = 1
for i in range(n):
    j = list(input())
    if i != 0:
        if j[0] == p:
            t+=1
    p = j[1]
print(t)