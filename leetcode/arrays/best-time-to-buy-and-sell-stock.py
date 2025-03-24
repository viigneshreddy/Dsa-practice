# Leetcode
# Problem name: best-time-to-buy-and-sell-stock
# Link:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Difficulty:Easy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)):
            if min > prices[i]:
                min = prices[i]
                min = prices[0]
                profit = 0
            profit = max(profit, prices[i] - min)
        return profit





