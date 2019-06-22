num=int(input('enter a number :'))
i=1
while i<=num :
	if num%i==0 and i!=num and i!=1 :
		print(num,'is not a prime number')
		break
	elif i==num:
		print(num,'is a prime number')
	i+=1