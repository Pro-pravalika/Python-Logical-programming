vowels = ['a','e','i','o','u']
def vowel(string):
	v_count = 0
	c_count = 0
	for x in string:
		if x in vowels:
			v_count +=1
		elif x!=' ':
			c_count+=1
	print(v_count)
		#print(c_count)
vowel('python is a easy to learn')