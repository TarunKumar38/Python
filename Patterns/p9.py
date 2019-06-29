r=1
while r<=5 :
	c=1
	result=''
	while c<=r :
		if r==1 or r==5 :
			result+='*'
		elif c==1 or c==r :
			result+='*'
		else :
			result+=' '
		c+=1
	print(result)
	r+=1