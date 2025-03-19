n = input().split(" ")
k = n[1]
n = n[0]
s = input().split(" ")
a=0
for j in s:
    if int(j) > 0:
        if int(j)>=int(s[int(k)-1]):
            a+=1
print(a)