import sys
sys.setrecursionlimit(10**5)
def find(arr1, arr2, res = []):
    if (not arr1) or (not arr2):
        return res
    num1, num2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(num1), arr2.index(num2)
    if num1 == num2:
        res.append(num1)
        return find(arr1[idx1 + 1:], arr2[idx2 + 1:], res)
    elif num1 > num2:
        arr1.pop(idx1)
    else:
        arr2.pop(idx2)
    return find(arr1, arr2, res)
n = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
ans = find(arr1, arr2)

print(len(ans))
if len(ans):
    print(*ans)