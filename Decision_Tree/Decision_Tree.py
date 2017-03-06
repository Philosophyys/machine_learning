from entropy import *

sleect_property = []
#tree = {}
R = []

def select(test_data):
	result = {}
	for i in range(len(test_data[0])-1):
		data = [[x[i],x[-1]] for x in test_data]
		result[i]=Select_Threshold(data)
	x = list(result.items())
	R = sorted(x,key = lambda x:x[1][1])
	return R[-1]

def _del(data):
	global R
	del data[R[0]]
	return data

def train(test_data,tree):
	while((len(test_data[0])-1) != 0):
		global R
		R = select(test_data)
		tree['class'] = R[0]
		print tree['class']
		print R
		tree['threshold'] = R[1][0]
		tree['sub_tree'] = {}
		data = list(map(_del,test_data)) 
		train(data,tree['sub_tree'])
	return tree