# Leetcode
# Problem name:remove-outermost-parentheses
# Link:https://leetcode.com/problems/remove-outermost-parentheses
#Difficulty:Easy

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        balance = 0

        for ch in s:
            if ch == ')':
                balance -= 1

            if balance > 0 :
                result += ch
                
            if ch == '(':
                balance += 1
            
        return result

