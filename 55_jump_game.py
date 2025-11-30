# 55. Jump Game
# =============== Recusrsion ================
from typing import List


# class Solution:
#     def helper(self, nums: List[int], goal) -> bool:
#         if goal == 0:
#             return True
        
#         for i in range(goal):
#             if i + nums[i] >= goal:
#                 return self.helper(nums, i)
#         return False
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         goal = n - 1
#         return self.helper(nums, goal)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1,0,4]
    print(solution.canJump(nums))  # Output: True