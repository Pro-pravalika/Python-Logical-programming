def triangle(stars):
	for x in range(stars):
		print(' '*(stars-x-1)+'*'*(2*x+1))
triangle(9)