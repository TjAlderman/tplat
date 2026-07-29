from typing import *

def majorityElement(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)

    if nums[0]==nums[n//2]:
        return nums[0]
    
    else:
        return nums[n//2+1]
        
nums = [3,2,3]
print(majorityElement(nums))
