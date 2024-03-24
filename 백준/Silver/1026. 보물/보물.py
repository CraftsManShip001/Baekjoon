a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
b.sort()
c.sort(reverse = True)
s = 0
for i in range(len(b)):
    s = s + (b[i]* c[i])
print(s)