r=1
n=int(input('Enter a number : '))
while r<=n :
	c=1
	result=''
	while c<=n :
		if r%2==0 :
			if c%2==0 :
				result+='1'
			else :
				result+='0'
		else :
			if c%2==0 :
				result+='0'
			else :
				result+='1'
		c+=1
	print(result)
	r+=1