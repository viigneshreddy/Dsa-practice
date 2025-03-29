# Leetcode
# Problem name:remove-duplicates-from-sorted-list
# Link:https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        else:
            curr = head
            while curr.next and curr:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            return head



