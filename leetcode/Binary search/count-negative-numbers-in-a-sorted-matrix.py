# Leetcode
# Problem name:count-negative-numbers-in-a-sorted-matrix
# Link:https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
#Difficulty:Easy

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count +=1
            
        return count
