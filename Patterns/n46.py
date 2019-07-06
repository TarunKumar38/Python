r=1
while r<=5 :
	c=1
	result=''
	while c<=r :
		if r%2==1 :
			result+=str(c)
		else :
			result+=str(r-c+1)
		c+=1
	print(result)
	r+=1