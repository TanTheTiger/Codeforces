n = int(input())
s = list(input())
t = 0
for i in s:
    if i == "A":
        t+=1
    else:
        t-=1
if t > 0:
    print("Anton")
elif t == 0:
    print("Friendship")
else:
    print("Danik")
