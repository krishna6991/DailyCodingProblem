"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8
time complexity o(n)
"""

def getMaxNonAdjacentElements(arr):
    inc,exc=0,0
    for num in arr:
        inc,exc = exc+num, max(inc,exc)
    return max(exc,inc)

print(getMaxNonAdjacentElements([2, 4, 6, 8]))
