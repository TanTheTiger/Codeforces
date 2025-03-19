s1 = list(input().lower())
s2 = list(input().lower())
if s1[-1] != s2[-1]:
    for i in range(0,len(s1)):
        if s1[i] > s2[i]:
            print(1)
        elif s2[i] > s1[i]:
            print(-1)
else:
    print(0)