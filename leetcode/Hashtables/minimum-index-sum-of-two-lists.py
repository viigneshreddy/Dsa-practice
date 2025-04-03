# Leetcode
# Problem name:minimum-index-sum-of-two-lists
# Link:https://leetcode.com/problems/minimum-index-sum-of-two-lists/
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {word: i for i, word in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, word in enumerate(list2):
            if word in index_map:
                total_index = j + index_map[word]
                if total_index < min_sum:
                    result = [word]
                    min_sum = total_index
                elif total_index == min_sum:
                    result.append(word)

        return result
