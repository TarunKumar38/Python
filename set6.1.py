num=int(input('enter any number : '))
sod=0
temp=num

while temp>0 :
	rem=temp%10
	sod=rem+sod
	temp=temp//10

tsod=sod
rsod=0
while tsod>0 :
	rem=tsod%10
	rsod=rem+rsod*10
	tsod=tsod//10

if num==(sod*rsod) :
	print(num,'is a magic number')
else :
	print(num,'is not a magic number')
	








