r=1
n=int(input('Enter a number (<=5) : '))
while r<=n :
	c=r
	result=''
	while c<r+n :
		result+=str(c)
		c+=1
	print(result)
	r+=1