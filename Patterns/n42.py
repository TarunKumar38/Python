r=1
while r<=5 :
	c=1
	dig=2
	result=''
	while c<=2*r-1 :
		result+=str(dig)
		if c>r-1:
			dig-=2
		else :
			dig+=2
		c+=1
	print(result)
	r+=1