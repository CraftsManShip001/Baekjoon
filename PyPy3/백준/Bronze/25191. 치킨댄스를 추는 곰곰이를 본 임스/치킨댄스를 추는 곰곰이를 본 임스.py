n = int(input())
n1,n2 = map(int, input().split())
s = n1//2 + n2

if n >= s :
    print(s)
else :
    print(n)