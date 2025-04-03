# Leetcode
# Problem name:count-primes
# Link:https://leetcode.com/problems/count-primes
#Difficulty:Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def countPrimes(self, n: int) -> int:
        a = 0
        if n <= 2:
            return 0
        else:
            is_prime = [True] * n
            is_prime[0] = is_prime[1] = False

            for i in range(2,int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n, i):
                        is_prime[j] = False

            return sum(is_prime)

