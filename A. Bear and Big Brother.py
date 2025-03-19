a = input().split(" ")
b = int(a[1])
a = int(a[0])
x=0
#Solve for when 3^x*a is greater than 2^x*b
while (3**x)*a <= (2**x)*b:
    x+=1
print(x)