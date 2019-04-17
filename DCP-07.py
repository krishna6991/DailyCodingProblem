"""
Run-length encoding and decoding of a string
"""

from collections import OrderedDict
import re

def encodingWithoutRep(string):
	dict = OrderedDict.fromkeys(string,0)

	for ch in string:
		dict[ch] +=1

	encoded_str = ''
	for key,value in dict.items():
		encoded_str = encoded_str + str(value) + key

	return encoded_str


"""
if the characters are repeatable
"""

def encoding(string):
	encoded_str=''
	ch =''
	count=0
	for i in range(0,len(string)):
		if ch==string[i]:
			count +=1
		else:
			if count!=0:
				encoded_str += str(count) + ch
			ch = string[i]
			count=1
	encoded_str += str(count) + ch
	return encoded_str



def decoding(string):
	decoded_str=''
	for num,char in re.findall(r'([0-9]+)([a-z])', string):
		decoded_str +=char*int(num)
	return decoded_str


if __name__=="__main__":
	input='wwwwaaadexxxxxxww'
	encoded = encoding(input)
	print(encoded)
	print(decoding(encoded))