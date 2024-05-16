def plus(an):
    x = 1
    for i in range(len(an)):
        x = x * an[i]
    return x
n = int(input())
arr = list(map(int,input().split()))
m = max(arr)
prime = [i for i in range(5000001)]
prime[1] = 1
for idx in range(2,5000000):
    if prime[idx] == idx:
        for i in range(idx * 2, 5000001,idx):
            if prime[i] == i:
                prime[i] = idx
for i in arr:
    now = []
    num = i
    while(num > 1):
        now.append(prime[num])
        num = num // prime[num]
    for j in now:
        print(j,end = ' ')
    print()