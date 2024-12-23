nums = [input() for _ in range(2)]
if nums[0] < nums[1]:
    print(-1)
elif nums[0] == nums[1]:
    print(0)
else:
    print(1)