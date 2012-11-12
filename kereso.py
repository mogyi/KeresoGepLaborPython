
#fajlbeolvasas es inicalizalas
lines = tuple(open("top_depth.txt", 'r'))
pagenumber = int(lines[0])

pages = []
csucsokbol =[[] for i in range(1,pagenumber+2)]
csucsokba =[[] for i in range(1,pagenumber+2)]
kifok = [0 for i in range(pagenumber)]

#oldalak beolvasasa
for i in range(1,pagenumber+1):
	actline = lines[i].split()
	pages.insert(int(actline[0]),actline[1])

linknumber = int(lines[pagenumber+1])

#graf beolvasasa
for i in range(pagenumber+2,linknumber-1):
	act = lines[i].split()
	forras = int(act[0])
	cel = int(act[1])
	csucsokbol[forras].append(cel)
	csucsokba[cel].append(forras)
	kifok[forras]=kifok[forras]+1


#pagerank kezdeti	
pagerank = [1/float(pagenumber) for i in range(1,pagenumber+1)]
#csucs pagerankje
def pr(i):
	szumma =0
	for csucs in csucsokba[i]:
		szumma = szumma + float(pagerank[csucs])/kifok[csucs]
	return szumma

#pagerenkek k=100-as iteracioval
def pagerankfunc(k=100,d=0.88):
	
	for n in range(k+1):
		temp = [1/float(pagenumber) for i in range(1,pagenumber+1)]
		for i in range(1,pagenumber+1):
			temp.insert(i,(float(d) * float(pr(i)) + float(1.00-d)/float(pagenumber)))
		for j in range(1,pagenumber+1):
			pagerank.insert(j,temp[j])
	

pagerankfunc(100,0.88)
output = open('page_rank_output.txt', 'w')
print>>output, pagenumber
for i in range(1,pagenumber+1):
	output.write("{} {} {}\n".format(i,pages[i-1],pagerank[i]))