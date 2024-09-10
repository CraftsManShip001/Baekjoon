n = int(input())
arr = list(map(int,input().split()))
result = 'Nice'
for i in range(1,n+1):
    num = arr.index(i)
    an = arr[:num]
    ans = an[:]
    an.sort(reverse = True)
    if ans == an:
        arr.remove(i)
    else:
        result = 'Sad'
        break
print(result)