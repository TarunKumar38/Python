num=int(input('enter a number '))
result=""
temp=num
rem=0

rem=temp%100
	
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
	rem=temp%100
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
rem=temp%1000
rem=rem//100
		
if rem==1:
	result="one hundred "+result
elif rem==2:
	result="two hundred "+result
elif rem==3:
	result="three hundred "+result
elif rem==4:
	result="four hundred "+result
elif rem==5:
	result="five hindred "+result
elif rem==6:
	result="six hundred "+result
elif rem==7:
	result="seven hundred "+result
elif rem==8:
	result="eight hundred "+result
elif rem==9:
	result="nine hundred "+result
	
temp=num
rem=temp%100000
rem=rem//1000
	
if rem==10:
	result="ten thousand "+result
elif rem==11:
	result="eleven thousand "+result
elif rem==12:
	result="twelve thousand "+result
elif rem==13:
	result="thirteen thousand "+result
elif rem==14:
	result="fourteen thousand "+result
elif rem==15:
	result="fifteen thousand "+result
elif rem==16:
	result="sixteen thousand "+result
elif rem==17:
	result="seventeen thousand "+result
elif rem==18:
	result="eighteen thousand "+result
elif rem==19:
	result="nineteen thousand "+result
elif rem==20:
	result="twenty thousand "+result
elif rem==30:
	result="thirty thousand "+result
elif rem==40:
	result="forty thousand "+result
elif rem==50:
	result="fifty thousand "+result
elif rem==60:
	result="sixty thousand "+result
elif rem==70:
	result="seventy thousand "+result
elif rem==80:
	result="eighty thousand "+result
elif rem==90:
	result="ninety thousand "+result
else :
		
	temp=num
	rem=temp%10000
	rem=rem//1000
	
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
	rem=temp%100000
	rem=rem//10000
			
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
rem=temp%10000000
rem=rem//100000
	
if rem==10:
	result="ten lakh "+result
elif rem==11:
	result="eleven lakh "+result
elif rem==12:
	result="twelve lakh "+result
elif rem==13:
	result="thirteen lakh "+result
elif rem==14:
	result="fourteen lakh "+result
elif rem==15:
	result="fifteen lakh "+result
elif rem==16:
	result="sixteen lakh "+result
elif rem==17:
	result="seventeen lakh "+result
elif rem==18:
	result="eighteen lakh "+result
elif rem==19:
	result="nineteen lakh "+result
elif rem==20:
	result="twenty lakh "+result
elif rem==30:
	result="thirty lakh "+result
elif rem==40:
	result="forty lakh "+result
elif rem==50:
	result="fifty lakh "+result
elif rem==60:
	result="sixty lakh "+result
elif rem==70:
	result="seventy lakh "+result
elif rem==80:
	result="eighty lakh "+result
elif rem==90:
	result="ninety lakh "+result
else :
		
	temp=num
	rem=temp%1000000
	rem=rem//100000
	
	if rem==1:
		result="one lakh "+result
	elif rem==2:
		result="two lakh "+result
	elif rem==3:
		result="three lakh "+result
	elif rem==4:
		result="four lakh "+result
	elif rem==5:
		result="five lakh "+result
	elif rem==6:
		result="six lakh "+result
	elif rem==7:
		result="seven lakh "+result
	elif rem==8:
		result="eight lakh "+result
	elif rem==9:
		result="nine lakh "+result
			
	temp=num
	rem=temp%10000000
	rem=rem//1000000
			
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
rem=temp%1000000000
rem=rem//10000000
	
if rem==10:
	result="ten crore "+result
elif rem==11:
	result="eleven crore "+result
elif rem==12:
	result="twelve crore "+result
elif rem==13:
	result="thirteen crore "+result
elif rem==14:
	result="fourteen crore "+result
elif rem==15:
	result="fifteen crore "+result
elif rem==16:
	result="sixteen crore "+result
elif rem==17:
	result="seventeen crore "+result
elif rem==18:
	result="eighteen crore "+result
elif rem==19:
	result="nineteen crore "+result
elif rem==20:
	result="twenty crore "+result
elif rem==30:
	result="thirty crore "+result
elif rem==40:
	result="forty crore "+result
elif rem==50:
	result="fifty crore "+result
elif rem==60:
	result="sixty crore "+result
elif rem==70:
	result="seventy crore "+result
elif rem==80:
	result="eighty crore "+result
elif rem==90:
	result="ninety crore "+result
else :
		
	temp=num
	rem=temp%100000000
	rem=rem//10000000
	
	if rem==1:
		result="one crore "+result
	elif rem==2:
		result="two crore "+result
	elif rem==3:
		result="three crore "+result
	elif rem==4:
		result="four crore "+result
	elif rem==5:
		result="five crore "+result
	elif rem==6:
		result="six crore "+result
	elif rem==7:
		result="seven crore "+result
	elif rem==8:
		result="eight crore "+result
	elif rem==9:
		result="nine crore "+result
			
	temp=num
	rem=temp%1000000000
	rem=rem//100000000
			
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
			
if num==0:
	result="zero"
				
print(result)