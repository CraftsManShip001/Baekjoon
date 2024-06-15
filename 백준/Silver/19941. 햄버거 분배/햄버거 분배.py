n,k = map(int,input().split())
arr = list(input())
hm = []
count = 0
for i in range(n):
    if arr[i] == 'P':
        num = i-k
        num2 = i+k+1
        for j in range(num,num2):
            if j < 0 or j >= n:
                continue
            if arr[j] == 'H' and not j in hm:
                hm.append(j)
                count += 1
                break
print(count)