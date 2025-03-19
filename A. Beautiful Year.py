y = int(input())
y+=1
l = [i for i in str(y)]
while len(set(l)) != 4:
    y+=1
    l=[i for i in str(y)]
print(y)