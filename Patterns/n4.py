r=1
n=int(input('Enter a number : '))
while r<=n :
	c=1
	result=''
	while c<=n :
		if r==1 or r==n :
			result+='1'
		elif c==1 or c==n :
			result+='1'
		else :
			result+='0'
		c+=1
	print(result)
	r+=1