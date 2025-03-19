n = int(input())
c = 0
for i in range(n):
    p = input().split(' ')
    q = int(p[1])
    p = int(p[0])
    if q-p >= 2:
        c+=1
print(c)
    