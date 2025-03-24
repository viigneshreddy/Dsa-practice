# Leetcode
# Problem name: move-zeroes
# Link:https:https://leetcode.com/problems/move-zeroes/
#Difficulty:Easy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        while start < len(nums):
            if nums[start] != 0:
                nums[end],nums[start] = nums[start],nums[end]
                start += 1
                end += 1
            else:
                start += 1





