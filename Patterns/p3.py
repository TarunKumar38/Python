r=1
while r<=10 :
	c=1
	result=''
	while c<=10 :
		if r==1 or r==10 :
			result+='*'
		elif c==1 or c==10 or c==r or c==11-r :
			result+='*'
		else :
			result+=' '
		c+=1
	print(result)
	r+=1