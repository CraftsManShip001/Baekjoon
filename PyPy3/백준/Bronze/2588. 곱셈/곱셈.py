a = int(input())
b = input()
c = []
for i in b:
    c.append(int(i) * a)
c.reverse()
for j in c:
    print(j)
print(a * int(b))