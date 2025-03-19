n = input().split(' ')
h=n[1]
n=n[0]
a = input().split(' ')
r = 0
for i in range(0,int(n)):
    if int(a[i]) > int(h):
        r += 2
    else:
        r += 1
print(r)