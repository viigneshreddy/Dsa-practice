# Hackerrank
# Problem name:Dynamic Array
# Link: https://www.hackerrank.com/challenges/dynamic-array
# Difficulty:Easy

def dynamicArray(n, queries):
    # Write your code here
    l = [[] for _ in range(n)]
    latsans = 0
    result = []

    for query in queries:
        a, x, y = query
        if a == 1:
            l[(x ^ latsans) % n].append(y)
        else:
            t = (x ^ latsans) % n
            latsans = l[t][y % len(l[t])]
            result.append(latsans)
    return result

