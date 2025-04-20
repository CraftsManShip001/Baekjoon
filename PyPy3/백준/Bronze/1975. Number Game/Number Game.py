t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for i in range(2,n + 1):
        num = n
        while num:
            if num % i == 0:
                res += 1
                num = num // i
            else:
                break
    print(res)