r=1
while r<=9 :
	c=1
	result=''
	while c<=4 :
		if r==5 :
			break
		result+=' '
		c+=1
	c=1
	if r==5 :
		while c<=9 :
			result+='*'
			c+=1
	else :
		result+='*'
	print(result)
	r+=1
r=1