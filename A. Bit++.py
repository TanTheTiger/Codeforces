n = int(input())
x = 0
for i in range(n):
    s = input()
    if s.find("+") != -1:
        x+=1
    else:
        x-=1
print(x)