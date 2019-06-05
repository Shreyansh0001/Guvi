num = input().split()
temp1 = int(num[0])+1
temp2 = int(num[1])
for i in range(temp1,temp2):
	temp = i
	sum =0
	while (i>0):
		new = i%10
		sum = new**3+sum
		i = i//10
	if sum == temp:
		print(temp, end=' ')
