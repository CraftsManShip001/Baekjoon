def hi(n,a,b,c):
    if n == 1:
        
        print(a,c)
    else:
        hi(n-1,a,c,b)
        print(a,c)
        hi(n-1,b,a,c)
n = int(input())
res = (2 ** n) -1
if n > 20:
    print(res)
    quit()
else:
    print(res)
    hi(n,1,2,3)