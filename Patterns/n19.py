from math import ceil
n=int(input('enter a nunber :  '))
value=list()
r=1
while r<=n :
	c=1
	v1=list()
	while c<=n :
		v1.append(0)
		c+=1
	value.append(v1)
	r+=1
srow=scol=0
erow=ecol=n-1

i=1
j=0
ans=1
while i<=ceil(n/2) :
	
	while j<=erow :
		value[srow][j]=ans
		j+=1
		ans+=1
		
	srow+=1
	j=srow
	
	while j<=ecol :
		value[j][ecol]=ans
		j+=1
		ans+=1
		
	ecol-=1
	j=ecol
	
	while j>=scol :
		value[erow][j]=ans
		j-=1
		ans+=1
		
	erow-=1
	j=erow
	
	while j>srow :
		value[j][scol]=ans
		j-=1
		ans+=1
	
	j=scol
	scol+=1
	
	i+=1
	
	
r=0
while r<n :
	c=0
	result=''
	while c<n :
		if value[r][c]//10==0 :
			result+=str(value[r][c])+'   '
		elif value[r][c]//100!=0 :
			result+=str(value[r][c])+' '
		else :
			result+=str(value[r][c])+'  '
		
		c+=1
	print(result)
	r+=1
	