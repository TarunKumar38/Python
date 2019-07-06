r=0
i=1
while r<=4 :
	c=1
	result=''
	while c<=2**r :
		result+=str(i)
		if i==9 :
			i=0
		i+=1
		c+=1
	print(result)
	r+=1