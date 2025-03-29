# Leetcode
# Problem name:jewels-and-stones
# Link:https://leetcode.com/problems/jewels-and-stones/
#Difficulty:Easy

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone = 0
        for i in jewels:
            for j in stones:
                if i == j: 
                    stone += 1
        return stone
        return result



