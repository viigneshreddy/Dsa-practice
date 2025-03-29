# Leetcode
# Problem name:defanging-an-ip-address
# Link:https://leetcode.com/problems/defanging-an-ip-address
#Difficulty:Easy

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.','[.]')
        return address




