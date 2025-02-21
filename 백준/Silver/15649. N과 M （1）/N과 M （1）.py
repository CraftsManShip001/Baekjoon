from itertools import permutations

n,m = map(int,input().split())

nums = [x for x in range(1,n+1)]
perms = list(permutations(nums, m))

for res in perms:
    for idx in range(m):
        print(res[idx],end = ' ')
    print()