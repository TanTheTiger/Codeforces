x = int(input())
o = 0
if x%5 != 0:
    o = ((x-(x%5))/5)+1
else:
    o = x/5
print(int(o))