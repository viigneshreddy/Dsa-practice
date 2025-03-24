# Leetcode
# Problem name: remove-element
# Link:https://leetcode.com/problems/remove-element
#Difficulty:Easy

class Solution:
    def removeElement(self, nums:List[int],val:int)-> int:
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k




