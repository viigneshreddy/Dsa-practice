# Leetcode
# Problem name:final-prices-with-a-special-discount-in-a-shop
# Link:https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop
#Difficulty:Easy

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
