# Leetcode
# Problem name:power-of-three
# Link:https://leetcode.com/problems/power-of-three
#Difficulty:Easy


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
