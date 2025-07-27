# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_index = 0 

        for k in range(1, len(nums)):
            if nums[k] != nums[insert_index]:
                insert_index += 1
                nums[insert_index] = nums[k]
                     
        return insert_index + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    print("Unique count:", k)
    print("Modified list:", nums[:k])   