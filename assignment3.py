
while True :
	year=int(input('enter year :'))
	if year>=1950 and year<=2019 :
		break

while True :
	month=int(input('enter month :'))
	if month>=1 and month<=12 :
		break

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
	dater=31
elif month==4 or month==6 or month==9 or month==11 :
	dater=30
else :
	if year%4==0 and year%100!=0 :
		dater=29
	elif year%400==0 :
		dater=29
	else :
		dater=28

while True :
	date=int(input('enter date : '))
	if date<=dater and date >0 :
		break


tdays=(year-1)*365
tdays+=(year-1)//4
tdays-=(year-1)//100
tdays+=(year-1)//400

temp=month-1

while temp>0:
	if temp==1 or temp==3 or temp==5 or temp==7 or temp==8 or temp==10 or temp==12 :
		tdays+=31
	elif temp==4 or temp==6 or temp==9 or temp==11 :
		tdays+=30
	else :
		if year%4==0 and year%100!=0 :
			tdays+=29
		elif year%400==0 :
			tdays+=29
		else :
			tdays+=28
	temp-=1
	
tdays+=(date-1)

day=tdays%7
da=''
if day==0:
	da='monday'
elif day==1 :
	da='tuesday'
elif day==2 :
	da='wednesday'
elif day==3 :
	da='thursday'
elif day==4 :
	da='friday'
elif day==5 :
	da='saturday'
elif day==6 :
	da='sunday'
	
temp=date%10
d=''
if temp==0 :
	d='th'
elif temp==1 :
	d='st'
elif temp==2 :
	d='nd'
elif temp==3 :
	d='rd'
elif temp==5 :
	d='th'
elif temp==6 :
	d='th'
elif temp==7 :
	d='th'
elif temp==8 :
	d='th'
elif temp==9 :
	d='th'

m=''
if month==1 :
	m='january'
elif month==2 :
	m='february'
elif month==3 :
	m='march'
elif month==4 :
	m='april'
elif month==5 :
	m='may'
elif month==6 :
	m='june'
elif month==7 :
	m='july'
elif month==8 :
	m='august'
elif month==9 :
	m='september'
elif month==10 :
	m='october'
elif month==11 :
	m='november'
elif month==12 :
	m='december'

result='on '+str(date)+d+' '+m+', '+str(year)+' has '+da

print(result)