i=1
while i<=10 :
	hours=int(input('enter hours : '))
	if hours>40 :
		pay=(hours-40)*12
		print('overtime pay = ',pay)
	else :
		print('no overtime pay')
	i+=1
