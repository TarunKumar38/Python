n=p=z=0
while True :
	num=input('enter a number (enter end to stop ) :')
	if num=='end' :
		print('positives = ',p)
		print('negatives = ',n)
		print('zeroes= ',z)
		break
	if int(num)>0 :
		p+=1
	elif int(num)<0 :
		n+=1
	else :
		z+=1
	
	