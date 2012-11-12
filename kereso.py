

lines = tuple(open("top_depth.txt", 'r'))
pagenumber = int(lines[0])
for i in range(1,pagenumber+1):
	actline = lines[i].split();
	print actline;
