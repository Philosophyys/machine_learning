from Decision_Tree import *
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

# data_1=[[x[0],x[-1]] for x in test_data]
# data_2=[[x[1],x[-1]] for x in test_data]
# data_3=[[x[2],x[-1]] for x in test_data]
# data_4=[[x[3],x[-1]] for x in test_data]
# print Select_Threshold(data_1)
# print Select_Threshold(data_2)
# print Select_Threshold(data_3)
# print Select_Threshold(data_4)

train(test_data)