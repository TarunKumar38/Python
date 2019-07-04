import random

teams={'Arsenal':'ENG','Astana':'KAZ','Atletico':'ESP','Barcelona':'ESP','Bate':'BLR','Bayern':'GER','Benfica':'POR','Chelsea':'ENG','Cska Moskva':'RUS','Dinamo Zagreb':'CRO','Dynamo Kyiv':'UKR','Galatasaray':'TUR','Gent':'BEL','Juventus':'ITA','Leverkusen':'GER','Lyon':'FRA','M Tel Aviv':'ISR','Malmo':'SWE','Manchester City':'ENG','Manchester United':'ENG','Monchengladbach':'GER','Olympiacos':'GRE','Paris':'FRA','Porto':'POR','PSV':'NED','Real Madrid':'ESP','Roma':'ITA','Sevilla':'ESP','Shakhtar Donetsk':'UKR','Valencia':'ESP','Wolfsburg':'GER','Zenit':'RUS'}

lteams=['Arsenal','Astana','Atletico','Bate','Cska Moskva','Dinamo Zagreb','Dynamo Kyiv','Galatasaray','Gent','Leverkusen','Lyon','M Tel Aviv','Malmo','Manchester City','Manchester United','Monchengladbach','Olympiacos','Porto','Real Madrid','Roma','Sevilla','Shakhtar Donetsk','Valencia','Wolfsburg']

def champ(champions,a,c):
	b=random.choice(a)
	c=champions[b]
	champions.pop(b)
	a.pop()
	return c
	
	
def rest(c):
	while len(c)!=4:
		
		a=random.choice(lteams)
		
		for j in range(len(c)) :
			
			if teams[a]==teams[c[j]]:
				break
			elif teams[a]!=teams[c[j]] and j==len(c)-1:
				c.append(a)
				lteams.remove(a)
				
	return c
	
champions=['Barcelona','Bayern','Benfica','Chelsea','Juventus','Paris','PSV','Zenit']

ga=[]
gb=[]
gc=[]
gd=[]
ge=[]
gf=[]
gg=[]
gh=[]

a=[0,1,2,3,4,5,6,7]
b=0

ga.append(champ(champions,a,ga))
gb.append(champ(champions,a,gb))
gc.append(champ(champions,a,gc))
gd.append(champ(champions,a,gd))
ge.append(champ(champions,a,ge))
gf.append(champ(champions,a,gf))
gg.append(champ(champions,a,gg))
gh.append(champ(champions,a,gh))

ga=rest(ga)
for i in ga :
	print(teams[i],i,sep='\t')
print('')
	
gb=rest(gb)
for i in gb :
	print(teams[i],i,sep='\t')
print('')
	
gc=rest(gc)
for i in gc :
	print(teams[i],i,sep='\t')
print('')
	
gd=rest(gd)
for i in gd :
	print(teams[i],i,sep='\t')
print('')
	
ge=rest(ge)
for i in ge :
	print(teams[i],i,sep='\t')
print('')
	
gf=rest(gf)
for i in gf :
	print(teams[i],i,sep='\t')
print('')
	
gg=rest(gg)
for i in gg :
	print(teams[i],i,sep='\t')
print('')
	
gh=gh+lteams
for i in gh :
	print(teams[i],i,sep='\t')









