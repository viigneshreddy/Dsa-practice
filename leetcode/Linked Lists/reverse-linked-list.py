# Leetcode
# Problem name:reverse-linked-list
# Link:https://leetcode.com/problems/reverse-linked-list/
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = rev
            rev = curr
            curr = next_node
        return rev


