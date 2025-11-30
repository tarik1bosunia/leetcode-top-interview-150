# 45. Jump Game II

from typing import List

# =============== Recursion ================

# class Solution:
#     def helper(self, nums: List[int], goal) -> int:
#         if goal == 0:
#             return 0
        
#         min_jumps = float('inf')
#         for i in range(goal):
#             if i + nums[i] >= goal:
#                 jumps = 1 + self.helper(nums, i)
#                 min_jumps = min(min_jumps, jumps)
#         return int(min_jumps)
    
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         goal = n - 1
#         return self.helper(nums, goal)





# =============== Memoization ==============



# class Solution:
#     def helper(self, nums: List[int], goal, dp) -> int:
#         if goal == 0:
#             return 0
        
#         if dp[goal] != -1:
#             return dp[goal]
        
#         min_jumps = float('inf')
#         for i in range(goal):
#             if i + nums[i] >= goal:
#                 jumps = 1 + self.helper(nums, i, dp)
#                 min_jumps = min(min_jumps, jumps)
                
#         dp[goal] = int(min_jumps)
#         return dp[goal]
    
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         goal = n - 1
#         dp = [-1] * n
#         return self.helper(nums, goal, dp)


# =============== Tabulation ==============

# class Solution:
    
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         goal = n - 1
#         dp = [-1] * n
        
#         dp[0] = 0
#         for j in range(1, n):
#             min_jumps = float('inf')
#             for i in range(j):
#                 if i + nums[i] >= j:
#                     jumps = 1 + dp[i]
#                     min_jumps = min(min_jumps, jumps)
#             dp[j] = int(min_jumps)
#         return dp[goal]


# =============== Greedy Optimal ==============
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        # we don't need to jump from the last index
        for i in range(n - 1):
            # update the farthest we can reach
            farthest = max(farthest, i + nums[i])

            # if we reached the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

                # small optimization: if we already can reach or pass last index, stop
                if current_end >= n - 1:
                    break

        return jumps


    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.jump(nums))  # Output: 2