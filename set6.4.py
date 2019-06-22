num=int(input('enter a number : '))
dig=0
sum=0
temp=num
flsum=0
msum=0

while temp>0 :
	dig=dig+1
	temp=temp//10

temp=num
i=1

while i<=dig :
	rem=temp%10
	
	if i==1 or i==dig :
		flsum=flsum+rem
	else :
		msum=msum+rem
		
	temp=temp//10
	i+=1
	
if msum==flsum :
	print(num,'is a cool number')
else :
	print(num,'is not a cool number')
		