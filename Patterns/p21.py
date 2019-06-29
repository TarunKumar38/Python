r=1
while r<=5 :
	c=1
	result=''
	while c<=5-r :
		result+=' '
		c+=1
	c=1
	while c<=r :
		result+='*'
		c+=1
	print(result)
	r+=1
r=1
while r<=4 :
	c=1
	result=''
	while c<=r :
		result+=' '
		c+=1
	c=1
	while c<=5-r :
		result+='*'
		c+=1
	print(result)
	r+=1
	