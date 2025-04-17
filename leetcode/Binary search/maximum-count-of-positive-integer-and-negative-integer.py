# Leetcode
# Problem name:find-the-k-th-character-in-string-game-i
# Link:https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer
#Difficulty:Easy

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        # Binary search to find the first positive number
        while l < r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
            else:
                r = m

        pos_count = len(nums) - l  # Everything after index l is positive

        # Now binary search to find first zero or positive to get negatives
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < 0:
                l = m + 1
            else:
                r = m

        neg_count = l  # Everything before index l is negative

        return max(pos_count, neg_count)
