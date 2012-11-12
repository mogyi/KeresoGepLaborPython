import numpy #tobbdimenzios tombok miatt

#fajlbeolvasas
lines = tuple(open("top_depth.txt", 'r'))
pagenumber = int(lines[0])
pages = []
csucsokbol =[list for i in range(pagenumber)]
csucsokba = [list for i in range(pagenumber)]
kifok = [0 for i in range(pagenumber)]
print kifok[200]

for i in range(1,pagenumber+1):
	actline = lines[i].split()
	pages.insert(int(actline[0]),actline[1])

linknumber = int(lines[pagenumber+1])


for i in range(0,linknumber):
	act = lines[i].split()
	csucsokbol.insert(int(act[0]),int(act[1]))
	csucsokba.insert(int(act[1]),int(act[0]))