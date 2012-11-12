import easygui as eg
import re as regexp

#fajlbeolvasas es inicalizalas
lines = tuple(open("page_rank_output.txt", 'r'))
pagenumber = int(lines[0])
pages=[]
pageranks=[]
eredmenyek=[]
valasz = []

#oldalak beolvasasa
for i in range(1,pagenumber+1):
	actline = lines[i].split()
	pages.insert(int(actline[0]),actline[1])
	pageranks.insert(int(actline[0]),actline[2])

reply = eg.enterbox(msg='Kereses')

#regexp kereses
pattern= regexp.compile('.*%s.*'%reply)
for url in pages:
	matchobj = pattern.search(url)
	if matchobj:
		eredmenyek.append(matchobj.group())

if (len(eredmenyek)>0):
	for e in eredmenyek:
		i = pages.index(e)
		#egyszerusegbol a pageranket elore raktam, konnyebb rendezni
		valasz.append("{} {} {} \n".format(pageranks[i],pages[i],i+1))
		valasz.sort()
	#csokkeno
	valasz.reverse()
	eg.textbox(text=valasz)
else:
	eg.textbox(text="Nem talalhato")

'''
try:
	i = pages.index(reply)
	eredmeny="{} {} {}\n".format(i+1,pages[i],pageranks[i])
except ValueError:
	eredmeny="Nem talalhato"
eg.textbox(text=eredmeny)
'''