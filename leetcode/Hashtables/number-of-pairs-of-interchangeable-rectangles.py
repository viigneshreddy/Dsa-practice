# Leetcode
# Problem name:number-of-pairs-of-interchangeable-rectangles
# Link:https:https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
#Difficulty:Medium

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import defaultdict

        ratio_count = defaultdict(int)
        result = 0

        for width, height in rectangles:
            ratio = width / height
            result += ratio_count[ratio]
            ratio_count[ratio] += 1

        return result



