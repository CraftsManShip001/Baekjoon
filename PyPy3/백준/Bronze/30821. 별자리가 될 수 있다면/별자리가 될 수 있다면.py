def find(n):
    if n == 1 or n == 0:
        return 1
    return n * find(n-1)

n = int(input())
print(find(n) // (find(n-5) * find(5)))