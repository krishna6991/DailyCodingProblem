"""

"""

from collections import deque

def printMaxWindowElement(arr,n,k):
    DQ =  deque()
    max_arr= []
    for i in range(k):
        while DQ and arr[i] >= arr[DQ[-1]]:
            DQ.pop()

        DQ.append(i)
    for i in range(k,n):
        max_arr.append(arr[DQ[0]])
        while DQ and DQ[0] <= i-k:
            DQ.popleft()

        while DQ and arr[i] >=arr[DQ[-1]]:
            DQ.pop()
        DQ.append(i)
    max_arr.append(arr[DQ[0]])
    return max_arr

if __name__=="__main__":
    arr = [1,2,3,4,2,3,8,6,4,3,7]
    k = 3
    arr=printMaxWindowElement(arr, len(arr), k)
    print(arr)
