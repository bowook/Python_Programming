def twoSum(nums, target):
    n = len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return True
    return False

print(twoSum(nums=[2,1,5,7], target=4))