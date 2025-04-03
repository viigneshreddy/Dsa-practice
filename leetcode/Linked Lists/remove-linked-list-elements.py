# Leetcode
# Problem name:remove-linked-list-elements
# Link:https://leetcode.com/problems/remove-linked-list-elements/
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)     # create a dummy node before head
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next  # skip the node
            else:
                current = current.next  # move forward

        return dummy.next

