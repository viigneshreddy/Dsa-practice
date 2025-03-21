# Leetcode
# Problem name:Remove Duplicates from sorted array
# Link: https://leetcode.com/problems/Remove Duplicates from sorted array
#Difficulty:Easy

class·Solution:
    def·removeDuplicates(self,·nums:·List
        j·=·1
        for·i·in·range(1,·len(nums)):
            if·nums[i]·!=·nums[i·-·1]:
                nums[j]·=·nums[i]
                         j·+=·1
        return·j



