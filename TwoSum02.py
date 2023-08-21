def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        sums = nums[i]
        targetMinus = target - sums
        if(targetMinus in nums[i+1:]):
            return True
    return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))