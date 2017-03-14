import numpy as np

def getdata(filename):
	input = file(filename,'r')
	data = input.readlines()
	xlists = []
	attributes = []
	attributes = data.pop(0).split(",")
	attributes[-1] = attributes[-1].strip()
	attributes = dict(zip(range(len(attributes)),attributes))
	print "Output:\nAttributes:\n%s"%attributes.values()
	for line in data:
		row =  line.split(",")
		row[-1] = row[-1].strip()
		xlists.append(row)
	data = np.array(xlists)
	istypes(data)

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
	print "number:\t%d\nstrings:\t%d\nother:\t%d"%(types[0],types[1],types[2])
