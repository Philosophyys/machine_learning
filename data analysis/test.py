from data_analysis import *
import numpy as np
import sys

input = file('F:\dataset.txt','r')
data = input.readlines()
xlists = []

for line in data:
	row =  line.split(",")
	row[-1] = row[-1].strip()
	xlists.append(row)

a = np.array(xlists)
istypes(a)