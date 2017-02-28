from entropy import *

def train(test_data):
	result = {}
	for i in range(len(test_data[0])-1):
		data = [[x[i],x[-1]] for x in test_data]
		result[i]=Select_Threshold(data)
	x = list(result.items())
	R = x.sort(key = bin(x[1][1][1]))
	print x[1][1][1]
	print result