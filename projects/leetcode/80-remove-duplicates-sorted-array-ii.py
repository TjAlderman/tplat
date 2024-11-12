from typing import *

def removeDuplicates(nums: List[int]) -> int:
    if len(nums)>2:
        idx = 0
        l1,l2 = nums[idx], nums[idx+1]
        for item in nums[2:]:
            if l1==l2==item:
                nums.remove(item)
            else:
                idx+=1
                l1,l2 = nums[idx], nums[idx+1]
    
    return len(nums)

nums = [0,0,1,1,1,1,2,3,3]
removeDuplicates(nums)
print(nums)