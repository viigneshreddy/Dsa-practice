# Leetcode
# Problem name:count-special-quadruplets
# Link:https://leetcode.com/problems/count-special-quadruplets
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for a,b,c,d in combinations(nums,4):
            if a + b + c == d:
                count += 1
        return count

