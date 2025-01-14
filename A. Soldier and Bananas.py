k = input().split(" ")
n = int(k[1])
w = int(k[2])
k = int(k[0])
for i in range(1,w+1):
    n -= (i*k)
if n >=0:
    print(0)
else:
    print(abs(n))