range=0
big=0
small=0


while True :
	num=input('enter a number (enter end to stop ) :')
	
	if num=='end' :
		print(range)
		break
	
	if int(num)>big :
		big=int(num)
	elif int(num)<small :
		small=int(num)
	
	
	range=big-small