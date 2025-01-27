while True :
    nums = list(map(int, input().split()))
    if sum(nums) == 0:
        break
    num = max(nums)
    nums.remove(num)
    if nums[0]**2 + nums[1]**2==num**2:
        print('right')
    else:
        print('wrong')