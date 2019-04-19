"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

Dynamic solution in o(n) time complexity
"""


def possibleDecodeWays(str):
    n = len(str)
    count = [0]*(n+1)
    if n==0:
        return 0
    for i in range(n+1):
        if i ==0:
            count[i]=1
            continue
        elif i==1:
            count[i]=1
            continue
        if (str[i-1] > '0'):
            count[i] = count[i-1]
        if (str[i-2] == '1' or (str[i-2] == '2' and str[i-1] < '7') ):
            count[i] += count[i-2]
    return count[n]

given_str = '111'
str = list(given_str)
ans = possibleDecodeWays(str)
print(ans)
