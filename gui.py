import easygui as eg

#fajlbeolvasas es inicalizalas
lines = tuple(open("page_rank_output.txt", 'r'))
pagenumber = int(lines[0])
pages=[]
pageranks=[]
#oldalak beolvasasa
for i in range(1,pagenumber+1):
	actline = lines[i].split()
	pages.insert(int(actline[0]),actline[1])
	pageranks.insert(int(actline[0]),actline[2])

reply = eg.enterbox(msg='Kereses')
i = pages.index(reply)
eredmeny="{} {} {}\n".format(i+1,pages[i],pageranks[i])
eg.textbox(text=eredmeny)