num=int(input('enter a number : '))
temp=num
flsum=0
msum=0

while temp>0 :
	rem=temp%10
	if temp==num or temp//10==0 :
		flsum=flsum+rem
	else :
		msum=msum+rem
	temp=temp//10
	
if msum==flsum :
	print(num,'is a cool number')
else :
	print(num,'is not a cool number')
