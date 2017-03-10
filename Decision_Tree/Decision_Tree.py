from entropy import *

sleect_property = []
R = []
correct = ()

def select(test_data):
	result = {}
	for i in range(len(test_data[0])-1):
		data = [[x[i],x[-1]] for x in test_data]
		result[i]=Select_Threshold(data)
	x = list(result.items())
	R = sorted(x,key = lambda x:x[1][1])
	return R[-1]

def split(test_data):
	global R
	data = [[],[]]
	for x in test_data:
		if float(x[R[0]]) <= float(R[1][0]):
			x.pop(int(R[0]))
			data[0].append(x)
		else:
			x.pop(int(R[0]))
			data[1].append(x)
	return data

def _train(test_data,tree):
	global R
	global correct
	print R
	if len(test_data) != 1:
		while((len(test_data[0])-1) != 0):
			R = select(test_data)
			tree['class'] = correct[R[0]]	
			del(correct[R[0]])
			tree['threshold'] = R[1][0]
			data = split(test_data)
			print data
			if len(data) != 0:
				for i in range(len(data[0])-1):
					tree[('sub_tree_'+str(i))]={}
					_train(data[i],tree[('sub_tree_'+str(i))])
	return tree

def train(test_data,tree):
	global correct
	correct = range(len(test_data[0])-1)
	_train(test_data,tree)
	return tree