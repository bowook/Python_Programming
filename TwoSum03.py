def twoSum(nums, target):
    nums = sorted(nums)
    last_index= len(nums)-1
    first_index = 0
    while first_index<last_index:
        if(nums[first_index]+nums[last_index] > target):
            last_index -= 1
        elif(nums[first_index]+ nums[last_index] < target):
            first_index += 1
        elif(nums[first_index] + nums[last_index] == target):
            return True
    return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))