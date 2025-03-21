t = int(input())
for i in range(t):
    a = input().split(" ")
    b = int(a[1])
    a = int(a[0])
    c = a
    if a < b:
        print(b-a)
    elif a == b or a%b == 0:
        print(0)
    else:
        #print(b*(-(-a//b))-a)
        print(b-a%b)