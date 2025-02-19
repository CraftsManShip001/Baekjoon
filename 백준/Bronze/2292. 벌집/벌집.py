n = int(input())
ans = 0
idx = 1
while True:
    ans += 1
    if idx >= n:
        break
    idx += ans * 6
print(ans)