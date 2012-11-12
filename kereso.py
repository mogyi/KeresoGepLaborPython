
#fajlbeolvasas es inicalizalas
lines = tuple(open("top_depth.txt", 'r'))
pagenumber = int(lines[0])
pages = []
csucsokbol =[[] for i in range(0,pagenumber+1)]
csucsokba =[[] for i in range(0,pagenumber+1)]
kifok = [0 for i in range(pagenumber)]

#oldalak beolvasasa
for i in range(1,pagenumber+1):
	actline = lines[i].split()
	pages.insert(int(actline[0]),actline[1])

linknumber = int(lines[pagenumber+1])

#gráf beolvasasa
for i in range(pagenumber+2,linknumber-1):
	act = lines[i].split()
	forras = int(act[0])
	cel = int(act[1])
	csucsokbol[forras].append(cel)
	csucsokba[cel].append(forras)
	kifok[forras]=kifok[forras]+1


#pagerank kezdeti	
pagerank = [1/pagenumber for i in range(0,pagenumber+1)]

