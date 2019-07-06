r=1
dig=1
while r<=5 :
	c=1
	result=''
	while c<=r :
		if dig//10==0 :
			result+=str(dig)+'  '
		elif dig//10!=0 :
			result+=str(dig)+' '
		dig+=1
		c+=1
	print(result)
	r+=1