# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        insert_index = 0 
        for j in range(length):
            if nums[j] != val:
                nums[insert_index] = nums[j]
                insert_index += 1
            j += 1
  
        return insert_index

if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    solution = Solution()
    k = solution.removeElement(nums, val)
    print(f"New length: {k}")
    print(f"Modified array: {nums[:k]}")  # Output: [2, 2]