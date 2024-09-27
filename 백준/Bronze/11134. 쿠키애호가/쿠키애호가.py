t = int(input())
for _ in range(t):
    n,c = map(int,input().split())
    cnt = n // c
    if n % c:
        cnt += 1
    print(cnt)