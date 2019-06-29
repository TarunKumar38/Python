r=5
while r>=1 :
	c=1
	result=''
	while c<=5-r :
		result+=' '
		c+=1
	c=1
	while c<=(2*r-1) :
		result+='*'
		c+=1
	print(result)
	r-=1