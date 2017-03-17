import numpy as np
import math
import pylab

def getdata(filename):
	'''
	function:get attributes and data
	input: the file location
	output: the tuple of (attributes, data)
	data's type is numpy.array
	ex: getdata('F:\dataset.txt')
	'''
	input = file(filename,'r')
	data = input.readlines()
	xlists = []
	attributes = []
	attributes = data.pop(0).split(",")
	attributes[-1] = attributes[-1].strip()
	attributes = dict(zip(range(len(attributes)),attributes))
	for line in data:
		row =  line.split(",")
		row[-1] = row[-1].strip()
		xlists.append(row)
	__data = np.array(xlists)
	return (attributes,__data)

def istypes(nparry):
	#get types of attributes
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
	print "Output:\nnumber:\t%d\nstrings:\t%d\nother:\t%d"%(types[0],types[1],types[2])

def calculate(data,num,type='number'):
#calculate mean & variance
	i = 0
	sum = 0
	mean = 0
	variance = 0
	if type == 'number':
		for data_line in data:
			if data_line[num] != '':
				sum += float(data_line[num])
				i+=1
			else:
				pass
		mean = sum/i
		sum = 0
		for data_line in data:
			if data_line[num] != '':
				sum += (float(data_line[num])-mean)**2
			else:
				pass
		variance = sum / i
	else :
		for data_line in data:
			if data_line[num] != '':
				pass
	return (mean,variance)

