n1 = list(input())
n2 = list(input())
s = ''
for i in range(len(n1)):
    if n1[i] != n2[i]:
        s += '1'
    else:
        s+= '0'
print(s)