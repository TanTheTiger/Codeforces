s1 = list(input().lower())
s2 = list(input().lower())
s1 = ''.join(s1)
s2 = ''.join(s2)
if s1 > s2:
    print(1)
elif s2 > s1:
    print(-1)
else:
    print(0)