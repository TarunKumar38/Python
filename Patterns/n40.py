r=1
while r<=5 :
	c=1
	if r%2==1 :
		i=1
	else :
		i=2
	result=''
	while c<=r :
		result+=str(i)
		i+=2
		c+=1
	print(result)
	r+=1