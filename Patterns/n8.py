r=1
n=int(input('Enter a number : '))
while r<=n :
	c=1
	result=''
	while c<=n :
		if r==c or c==n+1-r :
			result+='1'
		else :
			result+='0'
		c+=1
	print(result)
	r+=1