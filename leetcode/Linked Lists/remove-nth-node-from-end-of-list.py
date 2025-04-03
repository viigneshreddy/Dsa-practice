# Leetcode
# Problem name:remove-nth-node-from-end-of-list
# Link:https://leetcode.com/problems/remove-nth-node-from-end-of-list
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        for i in range(n):
            right = right.next
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next
