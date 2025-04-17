# Leetcode
# Problem name:intersection-of-two-arrays
# Link:https://leetcode.com/problems/intersection-of-two-arrays
#Difficulty:Easy


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for i in nums1:
            if i in nums2:
                res.add(i)
        
        return list(res)
