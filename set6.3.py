num=int(input('enter a number : '))
dig=0
sum=0
temp=num

while temp>0 :
	dig=dig+1
	temp=temp//10

temp=num
i=1
while i<=dig :
	rem=temp%10
	if i==1 or i==dig :
		sum=sum+rem
	temp=temp//10
	i+=1
	
print(sum)
		