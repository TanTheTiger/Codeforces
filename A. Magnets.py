n = int(input())
s = []
t = 1
for i in range(n):
    j = list(input())
    s.append(j[0])
    s.append(j[1])
s.pop(0)
s.pop(-1)
while len(s) != 0:
    if s[0] == s[1]:
        t+=1
    s.pop(1)
    s.pop(0)
print(t)