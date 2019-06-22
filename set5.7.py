num1=int(input('enter a number : '))
num2=int(input('enter another number : '))
i=1
while i<num1 :
	if num1%i==0 and num2%i==0 :
		hcf=i
	i+=1
	
lcm=num1*num2//hcf
print('lcm : ',lcm)
print('hcf : ',hcf)