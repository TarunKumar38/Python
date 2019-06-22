i=0
rem=0
res=0
dig=0
temp=0

while i<=500 :
	
	temp=i
	dig=0
	while temp>0:
		dig+=1
		temp//=10
		
	temp=i
	res=0
	
	while temp>0 :
		rem=temp%10
		res=res+(rem**dig)
		temp=temp//10
		
	if res==i :
		print(i)
	
		
	i=i+1