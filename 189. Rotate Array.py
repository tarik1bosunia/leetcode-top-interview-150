"https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150"

from typing import List
# 1. Slicing Solution
# Time: O(n)
# Space: O(n) (because of slicing copy)
# nums[:] = is used to modify the list in-place.
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # handle k > n

        nums[:] = nums[-k:] + nums[:-k]
        print(nums)
        
        
 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)      # Reverse all
        reverse(0, k - 1)      # Reverse first k
        reverse(k, n - 1)      # Reverse rest
       

if __name__ == "__main__":
    solution = Solution1()
    solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)        