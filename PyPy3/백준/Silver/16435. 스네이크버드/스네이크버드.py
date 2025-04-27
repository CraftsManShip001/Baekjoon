n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
for i in range(n):
    if(m >= arr[i]):
        m += 1
    else:
        break;
print(m)