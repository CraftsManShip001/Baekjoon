t = int(input())
for _ in range(t):
    n = int(input())
    name = []
    count = []
    for _ in range(n):
        a,b = input().split()
        name.append(a)
        count.append(int(b))
    print(name[count.index(max(count))])