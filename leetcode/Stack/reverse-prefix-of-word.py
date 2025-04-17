# Leetcode
# Problem name:reverse-prefix-of-word
# Link:https://leetcode.com/problems/reverse-prefix-of-word
#Difficulty:Easy

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        a = word.find(ch)

        if a == -1:
            return word
        
        else:
            reverse = word[:a+1][::-1]

            reverse += word[a+1:]

            return reverse

