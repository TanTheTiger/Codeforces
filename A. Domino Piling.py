n = input().split(" ")
m=int(n[0])
n=int(n[1])
if m*n%2 != 0:
    print(int((m*n-1)/2))
else:
    print(int(m*n/2))