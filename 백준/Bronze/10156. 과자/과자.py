k,n,m = map(int,input().split())
if m <= (k * n):
    print((k * n) - m)
else:
    print(0)