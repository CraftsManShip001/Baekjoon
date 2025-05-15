n = input()
arr = []
idx = 0
while idx < len(n):
    if n[idx] in ('a', 'e', 'i', 'o', 'u'):
        arr.append(n[idx])
        idx += 3
    else:
        arr.append(n[idx])
        idx += 1
print(''.join(arr))