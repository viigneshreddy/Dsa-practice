# Leetcode
# Problem name: median-of-two-sorted-arrays
# Link:https:https://leetcode.com/problems/median-of-two-sorted-arrays/
#Difficulty:Easy

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return (median(sorted(nums1 +nums2)))





