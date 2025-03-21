t = int(input())
for i in range(t):
    a = input().split(" ")
    b = int(a[1])
    a = int(a[0])
    c = a
    if a < b:
        print(b-a)
    elif a == b:
        print(a)
    else:
        while a%b != 0:
            a+=1
        print(a-c)