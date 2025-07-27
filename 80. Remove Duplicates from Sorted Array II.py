"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length <= 2:
            return nums_length
        insert_index = 2
        for k in range(2, len(nums)):
            if nums[k] != nums[insert_index - 2]:
                nums[insert_index] = nums[k]
                insert_index += 1
        return insert_index    
            
if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    k = solution.removeDuplicates(nums)
    print("Unique count:", k)
    print("Modified list:", nums[:k])   