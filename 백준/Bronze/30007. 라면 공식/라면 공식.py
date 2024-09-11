n = int(input())
for _ in range(n):
    a,b,x = map(int,input().split())
    print(((x-1) * a) + b)