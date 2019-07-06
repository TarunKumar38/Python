r=1
n=int(input('Enter a number : '))
while r<=n :
	c=1
	result=''
	while c<=n :
		result+=str(r)
		c+=1
	print(result)
	r+=1