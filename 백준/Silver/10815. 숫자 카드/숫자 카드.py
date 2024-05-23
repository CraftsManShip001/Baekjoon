n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
N.sort()


def bs(x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if N[mid] == x:
            return 1
        elif x < N[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return 0


for i in M:
    print(bs(i), end=' ')