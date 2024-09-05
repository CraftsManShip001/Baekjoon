n = int(input())
arr = []
alpa = {}
cnt = 0
next = 9
for _ in range(n):
    a = input()
    num = len(a) - 1
    for i in range(len(a)):
        if a[i] in alpa:
            alpa[a[i]] += (10 ** num)
        else:
            alpa[a[i]] = (10 ** num)
        num -= 1
    arr.append(a)
nums = sorted(alpa.items(),key = lambda x:x[1], reverse=True)
for i in nums:
    alpa[i[0]] = next
    next-=1
for i in arr:
    res = ''
    for j in range(len(i)):
        res += str(alpa[i[j]])
    cnt += int(res)
print(cnt)