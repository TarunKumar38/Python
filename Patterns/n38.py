r=1
while r<=5 :
	c=1
	result=''
	while c<=r :
		if c==1 or c==r or c==5 or r==5 :
			result+='1'
		else :
			result+='0'
		c+=1
	print(result)
	r+=1