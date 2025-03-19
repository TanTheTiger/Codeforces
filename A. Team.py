n = int(input())
s = 0
for i in range(n):
	p = input().split(" ")
	if int(p[0])+int(p[1])+int(p[2]) >= 2:
		s += 1
print(s)

