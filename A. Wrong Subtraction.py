n = input().split(" ")
k = int(n[1])
n = list(n[0])
n = [int(item) for item in n]
for i in range(k):
    if n[-1] != 0:
        n[-1] -= 1
    else:
        n.pop()
n = [str(item) for item in n]
print(''.join(n))