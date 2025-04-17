# Leetcode
# Problem name:find-the-k-th-character-in-string-game-i
# Link:https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
#Difficulty:Easy

class Solution:
    def kthCharacter(self, k: int) -> str:
        return ascii_lowercase[(k-1).bit_count()]
