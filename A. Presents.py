n = int(input())
p = input().split(' ')
p = [int(item) for item in p]
nl = []
for i in range(1,n+1):
    nl.append(p.index(i)+1)
nl = [str(item) for item in nl]
print(' '.join(nl))