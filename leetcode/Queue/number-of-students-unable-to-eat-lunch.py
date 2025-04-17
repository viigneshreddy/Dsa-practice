# Leetcode
# Problem name:number-of-students-unable-to-eat-lunch
# Link:https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
#Difficulty:Easy


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a = len(students)
        ctn = Counter(students)
        for i in sandwiches:
            if ctn[i] > 0:
                a-= 1
                ctn[i] -= 1
            else:
                return a


        return a
