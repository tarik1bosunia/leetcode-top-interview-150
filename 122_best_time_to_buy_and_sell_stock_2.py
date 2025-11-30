# ============== Recursion ==============

# from typing import List

# class Solution:
#     def helper(self, prices: List[int], n) -> int:
#         if n <= 0:
#             return 0
        
#         max_profit = 0
#         for i in range(n-1):
#             if prices[i] < prices[n - 1]:
#                 profit = (prices[n-1] - prices[i]) + self.helper(prices, i+1)
#                 max_profit = max(max_profit, profit)
#         return max_profit
        
#     def maxProfit(self, prices: List[int]) -> int:

#         n = len(prices)
#         return self.helper(prices, n)
    
# # Example usage:
# if __name__ == "__main__":
#     solution = Solution()
#     prices = [7,6,4,3,1]
#     print(solution.maxProfit(prices))  # Output: 4


# ============== Memoization ==============
# from typing import List

# class Solution:
#     def helper(self, prices: List[int], n, dp: List[int]) -> int:
#         if n <= 0:
#             return 0
        
#         max_profit = 0
#         if dp[n] != -1:
#             return dp[n]
#         for i in range(n-1):
#             if prices[i] < prices[n - 1]:
#                 profit = (prices[n-1] - prices[i]) + self.helper(prices, i+1, dp)
#                 max_profit = max(max_profit, profit)
#         dp[n] = max_profit
#         return dp[n]
        
#     def maxProfit(self, prices: List[int]) -> int:

#         n = len(prices)
#         dp = [-1] * (n + 1)
#         return self.helper(prices, n, dp)
    
# # Example usage:
# if __name__ == "__main__":
#     solution = Solution()
#     prices = [1,2,3,4,5]
#     print(solution.maxProfit(prices))  # Output: 4

# ============== Tabulation ==============
# from typing import List

# class Solution:
        
#     def maxProfit(self, prices: List[int]) -> int:

#         n = len(prices)
#         dp = [-1] * (n + 1)
#         dp[0] = 0
#         dp[1] = 0

#         for j in range(n + 1):
#             max_profit = 0
#             for i in range(n-1):
#                 if prices[i] < prices[j - 1]:
#                     profit = (prices[j-1] - prices[i]) + dp[i+1]
#                     max_profit = max(max_profit, profit)
#             dp[j] = max_profit
#         return dp[n]
    
# # Example usage:
# if __name__ == "__main__":
#     solution = Solution()
#     prices = [1,2,3,4,5]
#     print(solution.maxProfit(prices))  # Output: 4


# ============== Space Optimization ==============
# from typing import List

# class Solution:
        
#     def maxProfit(self, prices: List[int]) -> int:

#         n = len(prices)
        
#         if n <= 1:
#             return 0
        
#         dp = [0] * (n + 1)

#         for j in range(2, n + 1):
#             max_profit = dp[j-1]
#             sell_price = prices[j - 1]
            
#             for i in range(j-1):
#                 buy_price = prices[i]
#                 if buy_price < sell_price:
#                     profit = (sell_price - buy_price) + dp[i+1]
#                     max_profit = max(max_profit, profit)
#             dp[j] = max_profit
#         return dp[n]
    
# # Example usage:
# if __name__ == "__main__":
#     solution = Solution()
#     prices = [7,1,5,3,6,4]
#     print(solution.maxProfit(prices))  # Output: 7


# ============== Optimal Solution ==============
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print(solution.maxProfit(prices))  # Output: 7
