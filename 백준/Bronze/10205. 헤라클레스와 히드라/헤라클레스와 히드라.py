t = int(input())
for idx in range(t):
    n = int(input())
    arr = input()
    for i in range(len(arr)):
        if arr[i] == 'c':
            n += 1
        else:
            n -= 1
    print('Data Set %d:' %(idx+1))
    print(n)
    print()