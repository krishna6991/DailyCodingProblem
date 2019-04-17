# you have given an array print another with product of all array expect that ith position element.
#time complexity O(n)

import math
def productPuzzle(a, n):
    sum=0
    for i in range(n):
        sum +=math.log10(a[i])
    for i in range(n):
        print int(pow(10.00, sum-math.log10(a[i])))
    return

a = [1,2,3,4,4,5,6]
n = len(a)
productPuzzle(a,n)
