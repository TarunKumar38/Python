r=1
while r<=5 :
	c=1
	dig=1
	result=''
	while c<=2*r-1 :
		result+=str(dig)
		if c>r-1:
			dig-=1
		else :
			dig+=1
		c+=1
	print(result)
	r+=1