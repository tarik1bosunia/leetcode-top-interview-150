# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Dict



class Solution:
    # Boyer-Moore Algorithm
    # time complexity o(N), space complexity o(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1 
            
        return candidate  
               



# class Solution:
    # time complexity o(N), space complexity o(N)
    # def majorityElement(self, nums: List[int]) -> int:
    #     elements_count_map: Dict[int, int] = {}
    #     majority = len(nums)
    #     for num in nums:
    #         elements_count_map[num] = elements_count_map.get(num, 0) + 1
    #         if elements_count_map[num] > majority:
    #             return num
               
        # max_key = max(elements_count, key=elements_count.get)   
        # max_value = elements_count[max_key]
        # print("Max key:", max_key)
        # print("Max value:", max_value)
        # return max_key
                     

if __name__ == "__main__":
    solution = Solution()
    solution.majorityElement([2,2,1,1,1,2,2])
    