n = int(input())
arr = [1 for num in range(n) if int(input()) % 2 == 1]
print(len(arr))