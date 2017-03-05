from entropy import *

sleect_property=[]

def select(test_data):
	result = {}
	for i in range(len(test_data[0])-1):
		data = [[x[i],x[-1]] for x in test_data]
		result[i]=Select_Threshold(data)
	x = list(result.items())
	R = sorted(x,key = lambda x:x[1][1])
	return R[-1]

def train(test_data):
	for i in range(len(test_data[0])-1):
		select(data)