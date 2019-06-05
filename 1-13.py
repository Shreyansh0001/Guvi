num = int(input())
temp = num
lim = temp//2
count = 0
for i in range(1,lim):
	if (temp%i==0):
		count = count+1
if count >1:
	print("no")
else:
	print("yes")
