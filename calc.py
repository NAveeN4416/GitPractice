def multipler(m):
	def calculate(n):
 		return m * n

	return calculate

def divider(m):
	def calculate(n):
 		if n:	
			return m / n
		return None
	return calculate


three_multipl = multipler(3) 
print(three_multipl(3))
print(three_multipl(4))
