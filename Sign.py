class check():
	def ch(self,n):
		if (n>0):
			return("Positive")
		elif (n==0):
			return("Zero")
		else:
			return("Negative")
a=check()
m = int(input())
print(a.ch(m))
