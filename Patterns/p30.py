r=3
while r<=6 :
	c=1
	result=''
	while c<=6-r :
		result+=' '
		c+=1
	c=1
	while c<=(2*r-1) :
		result+='*'
		c+=1
	c=1
	while c<=(6-r)*2-1 :
		result+=' '
		c+=1
	c=1
	if r==6 :
		result='******codeforwin*****'
	else :
		while c<=(2*r-1) :
			result+='*'
			c+=1
	print(result)
	r+=1
r=1
while r<=12:
	c=1
	result=''
	while c<=r-1 :
		result+=' '
		c+=1
	c=1
	while c<=(2*(12-r)-1) :
		result+='*'
		c+=1
	print(result)
	r+=1