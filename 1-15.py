num = input().split()
temp1 = int(num[0]) +1
temp2 = int(num[1])
for i in range(temp1,temp2):
	if (i%2==0):
		print(i,end=' ')
