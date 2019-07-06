r=1
while r<=5 :
	c=r
	result=''
	while c<=5 :
		result+=str(c)
		c+=1
	c=r
	while c>1 :
		result+=str(c-1)
		c-=1
	print(result)
	r+=1