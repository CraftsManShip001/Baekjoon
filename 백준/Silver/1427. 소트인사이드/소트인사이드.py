n = input()
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))
arr.sort(reverse = True)
for i in arr:
    print(i,end = '')