a,b,c,d,n = map(int, input().split())

s = a+b+c+d

if s < (4 * n):
    print((4 * n) - s)
else:
    print(0)