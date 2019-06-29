r=1
while r<=5 :
	result=''
	c=1
	while c<r :
		result+=' '
		c+=1
	c=1
	while c<=6-r :
		result+='*'
		c+=1
	print(result)
	r+=1