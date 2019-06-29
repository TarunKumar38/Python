r=1
while r<=5 :
	c=1
	result=''
	while c<=r-1 :
		result+=' '
		c+=1
	c=1
	result+='*'
	while c<=(5-r)*2-1 :
		result+=' '
		c+=1
	if r==5 :
		None
	else :
		result+='*'
	print(result)
	r+=1
r=1
while r<=4 :
	c=1
	result=''
	while c<=4-r :
		result+=' '
		c+=1
	c=1
	result+='*'
	while c<=2*r-1 :
		result+=' '
		c+=1
	result+='*'
	print(result)
	r+=1