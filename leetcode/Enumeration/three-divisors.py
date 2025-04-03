# Leetcode
# Problem name:three-divisors
# Link:https://leetcode.com/problems/three-divisors
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        return count == 3

