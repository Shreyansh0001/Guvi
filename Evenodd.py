try:
	b = int(input())
	if(b%2==0):
		print("Even")
	elif(b%2==1):
		print("Odd")
except ValueError:
	print("Invalid")
