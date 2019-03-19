class check():
	def ch(self,n):
		if (n>0):
			return("Positive")
		elif (n==0):
			return("zero")
		else:
			return("negative")
a=check()
m = int(input())
print(a.ch(m))
