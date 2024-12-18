sum=0
n=100
while n>0:
	sum+=n
	if sum > 1000:
		break
	n=n-1
print(sum)