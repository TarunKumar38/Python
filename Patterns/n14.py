r=5
while r>0 :
	c=5
	result=''
	while c>0 :
		if r==5 or c==5 :
			result+='5'
		elif r==4 or c==4 :
			result+='4'
		elif r==3 or c==3 :
			result+='3'
		elif r==2 or c==2 :
			result+='2'
		elif r==1 or c==1 :
			result+='1'
		c-=1
	print(result)
	r-=1