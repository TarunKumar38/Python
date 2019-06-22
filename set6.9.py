num=int(input('enter a number :'))
temp=num
rem=0
i=0
n=0

while temp>0:
	rem=temp%10
	if rem==9 :
		rem=0
	else :
		rem+=1
	n=rem*10**i+n
	temp=temp//10
	i+=1

print(n)