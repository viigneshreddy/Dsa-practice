# Hackerrank
# Problem name:Arrays:Ds
# Link: https://www.hackerrank.com/challenges/arrays-ds
# Difficulty:Easy

def reverseArray(a):
    # Write your code here
    b =  []
    c = -1
    for i in range(len(a)):
        if c < (-i):
            b.append(a[c])
            c = c -1
    
    return b
