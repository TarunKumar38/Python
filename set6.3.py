num=int(input('enter a number : '))
sum=0
temp=num

while temp>0 :
	rem=temp%10
	if temp==num or temp//10==0 :
		sum=sum+rem
	temp=temp//10
	
print(sum)
