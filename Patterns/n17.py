r=1
while r<=5 :
	c=r
	result=''
	while c>0 :
		result+=str(c)
		c-=1
	c=1
	while c<=5-r :
		result+=str(c+1)
		c+=1
	print(result)
	r+=1