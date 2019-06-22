num=int(input('enter a number :'))
temp=num
rem=0
dig=0

while temp>0 :
	dig+=1
	temp=temp//10
	
temp=num
rev=0
while temp>0 :
	rem=temp%10
	rev=rev*10+rem
	temp=temp//10

temp=rev
i=1
s=0
result=''

while i<=dig :
	rem=temp%10
	if i==dig :
		result=result+str(rem)
	else :
		result=result+str(rem)+'+'
	s=s+rem
	temp=temp//10
	i+=1
	
result=result+'='+str(s)
print(result)
	