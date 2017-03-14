import numpy as np

def istypes(nparry):
	types = [0]*3
	(row,col) = nparry.shape
	for i in range(col-1):
		try:
			a = float(nparry[0][i+1])
			if isinstance(a,float):
				types[0] +=1
		except ValueError:
			if len(nparry[0][i+1]) > 0:
				types[1] +=1
			else:
				types[2] +=1
	print "Output:\nAttributes:\nnumber\t%d\nstrings\t%d\nother\t%d"%(types[0],types[1],types[2])
