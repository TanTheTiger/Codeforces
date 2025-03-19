n = []
for i in range(0,5):
    row = input().split(' ')
    n.append(row)
for i in range(0,5):
    for j in range(0,5):
        if n[i][j] == "1":
            print(abs(i-2)+abs(j-2))