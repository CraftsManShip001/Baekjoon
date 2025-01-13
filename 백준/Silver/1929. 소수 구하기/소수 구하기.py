import random
def miller(m):
    if m == 2 or m == 3:
        return 1
    if m <= 1 or m % 2 == 0:
        return 0
    r, d = 0, m - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(5):
        a = random.randint(2, m - 1)
        x = pow(a, d, m)
        if x == 1 or x == m - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, m)
            if x == m - 1: break
        else : return 0
    return 1

n,m = map(int,input().split())
for i in range(n,m+1):
    if miller(i):
        print(i)
