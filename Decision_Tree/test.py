from entropy import *
import string
#from math import *
input = file('D:\Program Files\Anaconda2\data.txt','r')
data = input.readlines()

i=0
test_data=[([0]*5) for x in range(150)]#150*[5*[0]]

for lines in data:
	line=string.split(lines,',')
	test_data[i][0]=line[0]
	test_data[i][1]=line[1]
	test_data[i][2]=line[2]
	test_data[i][3]=line[3]
	test_data[i][4]=line[4].strip('\n')
	i+=1

data_=[[x[0],x[-1]] for x in test_data]
print Select_Threshold(data_)

