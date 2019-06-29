r=1
while r<=5 :
	c=1
	result=''
	while c<=5-r :
		result+=' '
		c+=1
	c=1
	while c<=(2*r-1) :
		if r==1 or r==5 :
			result+='*'
		else :
			if c==1 or c==2*r-1 :
				result+='*'
			else :
				result+=' '
		c+=1
	print(result)
	r+=1