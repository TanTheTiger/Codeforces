s = input()
t = list(input())
t.reverse()
if s == ''.join(t):
    print("YES")
else:
    print("NO")