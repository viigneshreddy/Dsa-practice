# Leetcode
# Problem name: search-insert-position
# Link:https://leetcode.com/problems/search-insert-position
#Difficulty:Easy

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target and nums[i-1] < target:
                return i
            elif nums[-1] < target:
                return len(nums)
            elif nums[0]> target:
                return 0





