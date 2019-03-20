try:
	b = int(input())
	if(b%2==0 and b>=0):
		print("Even")
	elif(b%2==1 and b>=0):
		print("Odd")
	else:
		print("invalid")
except ValueError:
	print("invalid")
