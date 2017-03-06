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
	for x in test_data:
		if x[R[0]] <= R[1][0]
		data[0].append(x.pop[R[0]])
	else:
		data[1].append(x.pop[R[0]])
	return data

def _train(test_data,tree):
	while((len(test_data[0])-1) != 0):
		global R
		global correct
		R = select(test_data)
		print R
		tree['class'] = correct[R[0]]
		del(correct[R[0]])
		tree['threshold'] = R[1][0]
		tree['left_sub_tree'] = {}
		tree['right_sub_tree'] = {}		
		data = split(test_data)
		for x in data:
			_train(x,tree['sub_tree'])
	return tree

def train(test_data,tree):
	global correct
	correct = range(len(test_data[0])-1)
	_train(test_data,tree)
	return tree