e,s,m = map(int,input().split())
year = 1
n1,n2,n3 = 1,1,1
while True:
    if n1 == e and n2 == s and n3 == m:
        break
    if n1 == 15:
        n1 = 1
    else:
        n1 += 1
    if n2 == 28:
        n2 = 1
    else:
        n2 += 1
    if n3 == 19:
        n3 = 1
    else:
        n3 += 1
    year += 1
print(year)