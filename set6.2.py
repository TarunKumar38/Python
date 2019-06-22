num=int(input('enter a number : '))
dig=0
sum=0
temp=num

while temp>0 :
	dig=dig+1
	temp=temp//10
	
temp=num//10

while dig>2 :
	rem=temp%10
	sum=sum+rem
	temp=temp//10
	dig=dig-1

print(sum)
	