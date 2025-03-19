n = input().split(' ')
t = 0
for i in range(len(n)):
    for j in range(i+1,4):
        if n[i] == n[j]:
            t+=1
if t == 6:
    print(3)
elif t == 3:
    print(2)
else:
    print(t)