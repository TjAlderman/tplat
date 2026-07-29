from typing import *

def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for idx,item in enumerate(nums):
        # if item==val:
        while idx<len(nums) and nums[idx] == val:
            count += 1
            nums[idx:] = nums[idx+1:]
    return len(nums)-count

nums = [3,2,2,3]
val = 3
removeElement(nums,val)