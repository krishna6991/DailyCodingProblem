"""
given an array of non-negative integer, that represent an elevation map.
where each element is unit-width wall and the integer is height.
suppose it will rain and all spots between the walls get filled.\
Compute how many litre of water remain get traped? 
"""

#time complexity: o(n)
#space complexity: o(n)


def waterRemain(arr,n):
	left = [0]*n
	right =[0]*n

	water =0
	left[0]=arr[0]
	for i in range(1,n):
		left[i]=max(left[i-1], arr[i])

	right[n-1]=arr[n-1]
	for i in range(n-2,-1,-1):
		right[i] = max(right[i+1], arr[i])

	for i in range(0,n):
		water +=min(left[i],right[i]) - arr[i]
	return water

wall = [3,0,0,2,0,4]
n=len(wall)
print(waterRemain(wall,n))


"""
more optimized solution is instead of taking array of left and right max tower, we will take variable
"""

def waterTraped(arr,n):
	water=0
	left_max=0
	right_max=0
	low=0
	high=n-1

	while(low <=high):
		if(arr[low]< arr[high]):
			if(arr[low] >left_max):
				left_max=arr[low]
			else:
				water +=left_max -arr[low]
			low +=1
		else:
			if(arr[high] > right_max):
				right_max = arr[high]
			else:
				water +=right_max-arr[high]
			high -=1
	return water


wall = [3,0,0,2,0,4]
n=len(wall)
print(waterTraped(wall,n))

