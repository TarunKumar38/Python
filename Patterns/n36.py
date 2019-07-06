r=1
while r<=5 :
	c=1
	result=''
	while c<=r :
		if r%2==0 :
			result+='0'
		else :
			result+='1'
		c+=1
	print(result)
	r+=1