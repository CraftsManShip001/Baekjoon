r,c,n = map(int, input().split())
ans1 = r//n
if r % n != 0:
    ans1 += 1
ans2 = c//n
if c % n != 0:
    ans2 += 1
print(ans1*ans2)