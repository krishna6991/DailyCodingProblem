"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that 
returns the number of unique ways you can climb the staircase. The order of the steps matters.
"""

def total_ways(s):
	if s<=1:
		return s
	return total_ways(s-1) +total_ways(s-2)

n=4
print("total ways if only he can climb 1 or 2 stair at a time")
print(total_ways(n+1))

"""
instead of being able to climb 1 or 2 steps at a time, you could climb any number from a 
set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time
"""

def total_ways_random_step(s,x):
	DP = [0]*(s+1)
	DP[0]=DP[1]=1
	for i in range(2,s+1):
		for j in x:
			if i-j>=0:
				DP[i] += DP[i-j]
	return DP[s]

print(total_ways_random_step(7, [1,3,5]))