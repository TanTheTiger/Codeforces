n = int(input())
fridge = input().split(' ')
fridge = [int(item) for item in fridge]
s = 0
for i in fridge:
    s += i
s = s/n
print(s)