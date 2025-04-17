# Leetcode
# Problem name:count-pairs-whose-sum-is-less-than-target
# Link:https://leetcode.com/problems/https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target
#Difficulty:Easy

class class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1 
            
        return count
