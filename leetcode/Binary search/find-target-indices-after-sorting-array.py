# Leetcode
# Problem name:find-target-indices-after-sorting-array
# Link:https://leetcode.com/problems/find-target-indices-after-sorting-array
#Difficulty:Easy

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)

        return output
