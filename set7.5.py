i=1
m=21
while i<=4:
	while True :
		p=int(input('choose 1,2,3 or 4 matchsticks :'))
		if p>0 and p<5 :
			break
	
	print('computer chooses ',5-p)
	m-=5
	print('matchsticks left = ',m)
	
	i+=1

print('computer wins')