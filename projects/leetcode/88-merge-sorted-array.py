from typing import *

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Easy cases
        if n == 0:
            pass
        elif m == 0:
            nums1[:] = nums2[:]

        # O(n+m) iterate through both lists, right-shifting nums1 and inserting
        # from nums 2 where appropriate
        else:
            idx2 = 0
            for idx in range(m):
                if idx2 < n and nums1[idx] > nums2[idx2]:
                    nums1[idx + 1 :] = nums1[idx:-1]
                    nums1[idx] = nums2[idx2]
                    idx2 += 1
            if idx2 >= n:
                pass
            else:
                for idx in range(m, n + m):
                    if idx2 < n and (nums1[idx] > nums2[idx2] or idx >= idx2+m):
                        nums1[idx + 1 :] = nums1[idx:-1]
                        nums1[idx] = nums2[idx2]
                        idx2 += 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print(nums1)