def twoSum(nums, target):
    num_indices = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_indices:
            return [num_indices[complement], i]
        
        num_indices[num] = i
    
    return []

nums = [1, 2, 3, 5]
target = 4
result = twoSum(nums, target)

print(result)