r=0
list=[]
while r<6 :
	c=0
	l=[]
	while c<=r:
		l.append(0)
		c+=1
	list.append(l)
	r+=1
	
row=0
i=1
dig=1
while i<=3 :
	j=0
	while j<=row:
		list[row][j]=dig
		dig+=1
		j+=1
		
	row+=1
	j=row
	
	while j>=0 :
		list[row][j]=dig
		dig+=1
		j-=1
	
	row+=1
	i+=1
		
r=0
while r<6 :
	c=0
	result=''
	while c<=r :
		if list[r][c]//10==0 :
			result+=str(list[r][c])+'  '
		else :
			result+=str(list[r][c])+' '
		c+=1
	print(result)
	r+=1
