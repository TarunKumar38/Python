r=1
while r<=9 :
	c=1
	result=''
	if r==1 or r==5 or r==9 :
		result+=' '
		while c<=3 :
			result+='*'
			c+=1
		result+=' '
	else :
		result+='*'
		while c<=3 :
			result+=' '
			c+=1
		result+='*'
	print(result)
	r+=1