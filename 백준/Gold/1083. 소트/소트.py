n = int(input())
arr = list(map(int,input().split()))
s = int(input())
i = 0
while(1):
    if(s == 0 or i == n):
        break
    '''
    if(s > n):
        m = arr.index(max(arr[i:]))
    else:
    '''
    if(n - i >= n-(s + i+1)):
        m = arr.index(max(arr[i:s + i + 1]))
    else:
        m = arr.index(max(arr[i:]))
    if(m != i):
        temp = arr[m-1]
        arr[m-1] = arr[m]
        arr[m] = temp
        s -= 1
    else:
        i += 1
for i in arr:
    print(i,end = ' ')