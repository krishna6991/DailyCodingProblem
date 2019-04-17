"""
given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).
"""
brackets = {
	")":"(",
	"]":"[",
	"}":"{"
}

def is_well_formed(string):
	stack = []
	for ch in string:
		print(ch)
		if len(stack)==0:
			print("inserted ",ch)
			stack.append(ch)
		elif ch and stack[-1] in brackets and stack[-1]==brackets[ch]:
			print("popped ",ch,stack[-1])
			stack.pop()
		else:
			print("inserted ",ch)
			stack.append(ch)
	return True if len(stack)==0 else False

print(is_well_formed("([])[]({})"))