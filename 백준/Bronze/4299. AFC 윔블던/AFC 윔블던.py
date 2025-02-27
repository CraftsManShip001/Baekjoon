a, b = map(int, input().split())
if a < b:
    print(-1)
else:
    n1 = (a + b) // 2
    n2 = (a - b) // 2
    if (n1 + n2) == a and (n1 - n2) == b : 
        print(n1,n2)
    else:
        print(-1)