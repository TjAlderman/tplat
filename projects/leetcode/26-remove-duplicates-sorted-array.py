from typing import *

def removeDuplicates(nums: List[int]) -> int:
        n = len(nums)
        for idx,item in enumerate(nums):
            if idx<n-1 and item==nums[idx+1]:
                while idx+1<n and item==nums[idx+1]:
                    nums.remove(nums[idx+1])
                    n-=1
        return len(nums)

nums = [1,1]
removeDuplicates(nums)