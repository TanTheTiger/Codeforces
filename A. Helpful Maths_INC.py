s = input().split("+") #[3,2,1,2,3,2,3]
ns = []
l=0
while len(s) != 0:
    l=0
    for i in range(len(s)-1):
        if s[l]>s[i]:
            l=i
        elif s[l]==s[i]:
            l=i
    ns.append(s[l])
    s.pop(l)
print('+'.join(str(x) for x in ns))