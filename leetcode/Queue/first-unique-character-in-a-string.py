# Leetcode
# Problem name:first-unique-character-in-a-string
# Link:https://leetcode.com/problems/first-unique-character-in-a-string
#Difficulty:Easy


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
