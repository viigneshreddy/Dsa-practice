# Leetcode
# Problem name:power-of-two
# Link:https://leetcode.com/problems/power-of-two
#Difficulty:Easy

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
