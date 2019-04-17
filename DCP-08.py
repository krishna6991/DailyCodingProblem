"""
the edit distance between two strings refers to the minimum number of character insetions,
deletion, and subsitution.
"""
def min_edit_distance(str1, str2):
	if(str1==str2):
		return 0
	if not str1:
		return len(str2)
	if not str2:
		return len(str1)

	if(str1[0]==str2[0]):
		return min_edit_distance(str1[1:], str2[1:])

	return 1+ min(
		min_edit_distance(str1[1:], str2),  #deletion
		min_edit_distance(str1, str2[1:]), 	#insertion
		min_edit_distance(str1[1:], str2[1:]) #subsitution
		)

str1 = "kitten"
str2 = "sitting"

val = min_edit_distance(str1, str2)
print(val)