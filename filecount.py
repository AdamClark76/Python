from os import listdir

totalfiles = listdir(r'c:temp')

d = {}
for fl in totalfiles:
	if fl in d:
		d[fl] +=1
	else:
		d[fl] =1


for  x,y in d.items():
	if y>1:
		print x
	
print "total is:",len(d)

