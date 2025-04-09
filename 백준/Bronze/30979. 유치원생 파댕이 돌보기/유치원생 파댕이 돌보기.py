t = int(input())
n = int(input())
arr = list(map(int, input().split()))

if t <= sum(arr):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")