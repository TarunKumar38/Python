r=1
n=int(input('Enter a number : '))
while r<=n :
	c=1
	result=''
	while c<=n :
		if (r==1 or r==n) and (c!=1 and c!=n) :
			result+='1'
		elif (c==1 or c==n) and (r!=1 and r!=n) :
			result+='1'
		else :
			result+='0'
		c+=1
	print(result)
	r+=1