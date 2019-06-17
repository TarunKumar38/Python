num=int(input("enter a number : "))
result=""
temp=num
rem=temp%10

if rem==1:
	result="one"	
elif rem==2:
	result="two"
elif rem==3:
	result="three"
elif rem==4:
	result="four"
elif rem==5:
	result="five"
elif rem==6:
	result="six"
elif rem==7:
	result="seven"
elif rem==8:
	result="eight"
elif rem==9:
	result="nine"
		
temp=num
rem=temp%10**2
rem=rem//10**0
		
if rem==10 :
	result="ten"
elif rem==11 :
	result="eleven"
elif rem==12 :
	result="twelve"
elif rem==13 :
	result="thirteen"
elif rem==14 :
	result="fourteen"
elif rem==15 :
	result="fifteen"
elif rem==16 :
	result="sixteen"
elif rem==17 :
	result="seventeen"
elif rem==18 :
	result="eighteen"
elif rem==19 :
	result="nineteen"
elif rem==20 :
	result="twenty"
else :
	temp=num
	rem=temp%10
	
	if rem==1:
		result="one"	
	elif rem==2:
		result="two"
	elif rem==3:
		result="three"
	elif rem==4:
		result="four"
	elif rem==5:
		result="five"
	elif rem==6:
		result="six"
	elif rem==7:
		result="seven"
	elif rem==8:
		result="eight"
	elif rem==9:
		result="nine"
		
	temp=num
	rem=temp%10**2
	rem=rem//10
	
	if rem==2 :
		result="twenty "+result
	elif rem==3 :
		result="thirty "+result
	elif rem==4 :
		result="forty "+result
	elif rem==5 :
		result="fifty "+result
	elif rem==6 :
		result="sixty "+result
	elif rem==7 :
		result="seventy "+result
	elif rem==8 :
		result="eighty "+result
	elif rem==9 :
		result="ninety "+result
		
temp=num
rem=temp%10**3
rem=rem//10**2

if rem==1:
	result="one hundred and "+result
elif rem==2:
	result="two hundred and "+result
elif rem==3:
	result="three hundred and "+result
elif rem==4:
	result="four hundred and "+result
elif rem==5:
	result="five hindred and "+result
elif rem==6:
	result="six hundred and "+result
elif rem==7:
	result="seven hundred and "+result
elif rem==8:
	result="eight hundred and "+result
elif rem==9:
	result="nine hundred and "+result
	
temp=num
rem=temp%10**6
rem=rem//10**3

if rem==100 :
	result="one hundred thousand "+result
elif rem==200 :
	result="two hundred thousand "+result
elif rem==300 :
	result="three hundred thousand "+result
elif rem==400 :
	result="four hundred thousand "+result
elif rem==500 :
	result="five hundred thousand "+result
elif rem==600 :
	result="six hundred thousand "+result
elif rem==700 :
	result="seven hundred thousand "+result
elif rem==800 :
	result="eight hundred thousand "+result
elif rem==900 :
	result="nine hundred thousand "+result
else :
	
	temp=num
	rem=temp%10**5
	rem=rem//10**3

	if rem==10 :
		result="ten thousand "+result
	elif rem==11 :
		result="eleven thousand "+result
	elif rem==12 :
		result="twelve thousand "+result
	elif rem==13 :
		result="thirteen thousand "+result
	elif rem==14 :
		result="fourteen thousand "+result
	elif rem==15 :
		result="fifteen thousand "+result
	elif rem==16 :
		result="sixteen thousand "+result
	elif rem==17 :
		result="seventeen thousand "+result
	elif rem==18 :
		result="eighteen thousand "+result
	elif rem==19 :
		result="nineteen thousand "+result
	elif rem==20 :
		result="twenty thousand "+result
	elif rem==30 :
		result="thirty thousand "+result
	elif rem==40 :
		result="forty thousand "+result
	elif rem==50 :
		result="fifty thousand "+result
	elif rem==60 :
		result="sixty thousand "+result
	elif rem==70 :
		result="seventy thousand "+result
	elif rem==80 :
		result="eighty thousand "+result
	elif rem==90 :
		result="ninety thousand "+result
	else :
	
		temp=num
		rem=temp%10**4
		rem=rem//10**3

		if rem==1:
			result="one thousand "+result
		elif rem==2:
			result="two thousand "+result
		elif rem==3:
			result="three thousand "+result
		elif rem==4:
			result="four thousand "+result
		elif rem==5:
			result="five thousand "+result
		elif rem==6:
			result="six thousand "+result
		elif rem==7:
			result="seven thousand "+result
		elif rem==8:
			result="eight thousand "+result
		elif rem==9:
			result="nine thousand "+result
		
		temp=num
		rem=temp%10**5
		rem=rem//10**4
	
		if rem==2 :
			result="twenty "+result
		elif rem==3 :
			result="thirty "+result
		elif rem==4:
			result="forty "+result
		elif rem==5 :
			result="fifty "+result
		elif rem==6 :
			result="sixty "+result
		elif rem==7:
			result="seventy "+result
		elif rem==8 :
			result="eighty "+result
		elif rem==9:
			result="ninety "+result
		
	temp=num
	rem=temp%10**6
	rem=rem//10**5

	if rem==1:
		result="one hundred and "+result
	elif rem==2:
		result="two hundred and "+result
	elif rem==3:
		result="three hundred and "+result
	elif rem==4:
		result="four hundred and "+result
	elif rem==5:
		result="five hundred and "+result
	elif rem==6:
		result="six hundred and "+result
	elif rem==7:
		result="seven hundred and "+result
	elif rem==8:
		result="eight hundred and "+result
	elif rem==9:
		result="nine hundred and "+result
	
temp=num
rem=temp%10**9
rem=rem//10**6

if rem==100 :
	result="one hundred million "+result
elif rem==200 :
	result="two hundred million "+result
elif rem==300 :
	result="three hundred million "+result
elif rem==400 :
	result="four hundred million "+result
elif rem==500 :
	result="five hundred million "+result
elif rem==600 :
	result="six hundred million "+result
elif rem==700 :
	result="seven hundred million "+result
elif rem==800 :
	result="eight hundred million "+result
elif rem==900 :
	result="nine hundred million "+result
else :
	
	temp=num
	rem=temp%10**8
	rem=rem//10**6

	if rem==10 :
		result="ten million "+result
	elif rem==11 :
		result="eleven million "+result
	elif rem==12 :
		result="twelve million "+result
	elif rem==13 :
		result="thirteen million "+result
	elif rem==14 :
		result="fourteen million "+result
	elif rem==15 :
		result="fifteen million "+result
	elif rem==16 :
		result="sixteen million "+result
	elif rem==17 :
		result="seventeen million "+result
	elif rem==18 :
		result="eighteen million "+result
	elif rem==19 :
		result="nineteen million "+result
	elif rem==20 :
		result="twenty million "+result
	elif rem==30 :
		result="thirty million "+result
	elif rem==40 :
		result="forty million "+result
	elif rem==50 :
		result="fifty million "+result
	elif rem==60 :
		result="sixty million "+result
	elif rem==70 :
		result="seventy million "+result
	elif rem==80 :
		result="eighty million "+result
	elif rem==90 :
		result="ninety million "+result
	else :
	
		temp=num
		rem=temp%10**7
		rem=rem//10**6

		if rem==1:
			result="one million "+result
		elif rem==2:
			result="two million "+result
		elif rem==3:
			result="three million "+result
		elif rem==4:
			result="four million "+result
		elif rem==5:
			result="five million "+result
		elif rem==6:
			result="six million "+result
		elif rem==7:
			result="seven million "+result
		elif rem==8:
			result="eight million "+result
		elif rem==9:
			result="nine million "+result
		
		temp=num
		rem=temp%10**8
		rem=rem//10**7
	
		if rem==2 :
			result="twenty "+result
		elif rem==3 :
			result="thirty "+result
		elif rem==4:
			result="forty "+result
		elif rem==5 :
			result="fifty "+result
		elif rem==6 :
			result="sixty "+result
		elif rem==7:
			result="seventy "+result
		elif rem==8 :
			result="eighty "+result
		elif rem==9:
			result="ninety "+result
		
	temp=num
	rem=temp%10**9
	rem=rem//10**8

	if rem==1:
		result="one hundred and "+result
	elif rem==2:
		result="two hundred and "+result
	elif rem==3:
		result="three hundred and "+result
	elif rem==4:
		result="four hundred and "+result
	elif rem==5:
		result="five hundred and "+result
	elif rem==6:
		result="six hundred and "+result
	elif rem==7:
		result="seven hundred and "+result
	elif rem==8:
		result="eight hundred and "+result
	elif rem==9:
		result="nine hundred and "+result
	
print(result)