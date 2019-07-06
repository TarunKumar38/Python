r=1
n=int(input('Enter a number : '))
i=1
while r<=n :
	c=1
	result=''
	while c<=n :
		result+=str(i)+'	'
		c+=1
		i+=1
	print(result)
	r+=1