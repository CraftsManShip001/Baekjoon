n,m = map(int, input().split())
ans = ''
overten='ABCDEF'
if n == 0:
    print(0)
    exit()
while n != 0:
    if (n%m) > 9:
        ans += overten[(n%m) % 10]
    else:
        ans += str(n%m)
    n //= m
print(ans[::-1])