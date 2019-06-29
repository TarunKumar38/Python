r=1
while r<=5 :
	c=1
	result=''
	while c<=6-r :
		if r==1 or r==5 :
			result+='*'
		elif c==1 or c==6-r :
			result+='*'
		else :
			result+=' '
		c+=1
	print(result)
	r+=1