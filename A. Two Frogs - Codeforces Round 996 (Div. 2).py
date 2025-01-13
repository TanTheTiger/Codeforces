t = int(input())
for i in range(t):
    n = input().split(" ")
    a = int(n[1])
    b = int(n[2])
    n = int(n[0])
    if a>b:
        if (a-b)%2 == 0:
            #Odd Gap
            print("Yes")
        else:
            #Even Gap/No Gap: "a-b" == 1
            print("No")
    else:
        if (b-a)%2 == 0:
            #Odd Gap
            print("Yes")
        else:
            #Even Gap/No Gap: "a-b" == 1
            print("No")