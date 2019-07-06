r=1
while r<=9 :
	c=1
	result=''
	while c<=9 :
		if c==1 or c==9 or r==1 or r==9 :
			result+='5'
		elif c==2 or c==8 or r==2 or r==8 :
			result+='4'
		elif c==3 or c==7 or r==3 or r==7 :
			result+='3'
		elif c==4 or c==6 or r==4 or r==6 :
			result+='2'
		elif c==5 or c==5 or r==5 or r==5 :
			result+='1'
		c+=1
	print(result)
	r+=1
