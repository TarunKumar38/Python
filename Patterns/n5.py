r=1
n=int(input('Enter odd number : '))
while r<=n :
	c=1
	result=''
	while c<=n :
		if r==n//2+1 and c==n//2+1 :
			result+='0'
		else :
			result+='1'
		c+=1
	print(result)
	r+=1