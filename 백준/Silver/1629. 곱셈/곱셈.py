def result(n,num):
    if num == 1:
        return n % c
    elif num % 2:
        num -= 1
        return ((result(n,num // 2) ** 2) * n) % c
    else:
        return ((result(n,num // 2) ** 2)) % c
a,b,c = map(int,input().split())
print(result(a,b))