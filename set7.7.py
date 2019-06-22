num=int(input('enter a number :'))
roct=0
rem=0

while num>0 :
	rem=num%8
	roct=roct*10+rem
	num=num//8
	
oct=0

while roct>0:
	rem=roct%10
	oct=oct*10+rem
	roct//=10
	
print('octal equivalent =',oct)