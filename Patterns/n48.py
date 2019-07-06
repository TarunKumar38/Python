r=1
while r<=5 :
	c=1
	result=''
	while c<=r :
		result+=str(c)
		c+=1
	c=1
	while c<=8-(2*(r-1)) :
		result+=' '
		c+=1
	c=1
	while c<=r :
		result+=str(r-c+1)
		c+=1
	print(result)
	r+=1