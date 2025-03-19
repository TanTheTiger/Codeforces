t = int(input())
for i in range(t):
    a = input().split(" ")
    b = int(a[1])
    a = int(a[0])
    c = a
    while a%b != 0:
        a+=1
    print(a-c)