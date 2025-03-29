# Leetcode
# Problem name:final-value-of-variable-after-performing-operations
# Link:https://leetcode.com/problems/final-value-of-variable-after-performing-operations
#Difficulty:Easy

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in operations:
            if i == 'X++' or i == '++X':
                X += 1
            else:
                X -= 1
        return X




