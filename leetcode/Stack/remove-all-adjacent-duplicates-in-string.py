# Leetcode
# Problem name:remove-all-adjacent-duplicates-in-string
# Link:https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
#Difficulty:Easy

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i  = 0

        while i < len(s):
            if(
                stack and
                stack[-1] == s[i]
            ):
                stack.pop()
            else:
                stack.append(s[i])
            
            i += 1
        
        return "".join(stack)
