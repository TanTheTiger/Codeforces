n = int(input())
s = list(input())
d = 0
o = 0
for i in range(0,n):
    if i != 0:
        if s[i] == s[d]:
            o+=1
        else:
            d = i
print(o)