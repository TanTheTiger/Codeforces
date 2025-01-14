s = list(input())
v = 0
for i in range(0,len(s)):
    if s[i].isupper() is True:
        v+=1
    else:
        v-=1
if v > 0:
    print(''.join(s).upper())
else:
    print(''.join(s).lower())