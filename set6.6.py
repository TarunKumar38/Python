num=int(input('enter a number :'))
temp=num
i=1
j=1
while j<=num:
	i=1
	while i<=j :
		
		if j%i==0 and i!=j and i!=1 :
			break
			
		elif i==j and i!=1 :
			
			while True :
				if temp%i==0:
					print(i)
					temp=temp//i
				else :
					break
		
		i+=1
	j+=1