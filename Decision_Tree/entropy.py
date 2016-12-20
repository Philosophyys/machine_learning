from math import *
import copy
def Select_Threshold(data):
	sort_data=sorted(data,key=lambda x:x[0])
	fore_value=sort_data[0][0]
	fore_property=sort_data[0][1]
	un_threshold=[]
	for data_ in sort_data:
		back_value=data_[0]
		back_property=data_[1]
		if back_property!=fore_property:
			un_threshold.append((float(fore_value)+float(back_value))/2)
			fore_value=back_value
			fore_property=back_property
		else:
			fore_value=back_value
			fore_property=back_property
	return Information_Gain_Ratio(sort_data,undetermined_threshold=un_threshold,types='continue')

def Information_Gain_Ratio(data,undetermined_threshold=[],types='discrete'):
	if types=='discrete':
		properties=list(set([x[0] for x in data]))
		h_d_a=0
		for property in properties:
			property_num=[x[0] for x in data].count(str(property))
			property_probably=float(property_num+0.001)/len(data)
			h_d_a-=property_probably*log(property_probably,2)
		information_gain_ratio=Information_Gain(data)/h_d_a
		return information_gain_ratio

	elif types=='continue':
		adjust_data=copy.deepcopy(data)
		undetermined_information_gain_ratio=[]
		for u_t in undetermined_threshold:
			for i in xrange(len(data)):
				if u_t >= float(data[i][0]):
					adjust_data[i][0]='1'
				else:
					adjust_data[i][0]='0'
			undetermined_information_gain_ratio.append(Information_Gain_Ratio(adjust_data))
		max_information_gain_ratio=undetermined_information_gain_ratio[0]
		max_index=0
		index=0
		for u_i_g_r in undetermined_information_gain_ratio:
			if max_information_gain_ratio < u_i_g_r:
				max_information_gain_ratio=u_i_g_r
				max_index=index
				index+=1
			else:
				index+=1
	 	return (undetermined_threshold[max_index],max_information_gain_ratio)
	else:
		raise AttributeError

def Information_Gain(data):
	information_gain=Entropy(data)-Conditional_Entropy(data)
	return information_gain

def Entropy(data):
	categories=list(set([x[-1] for x in data]))
	h=0
	for category in categories:
		category_num=[x[-1] for x in data].count(category)
		probably=float(category_num+0.001)/len(data)
		h-=probably*log(probably,2)
	return h

def Conditional_Entropy(data):
	properties=list(set([x[0] for x in data]))
	categories=list(set([y[-1] for y in data]))
	h_d_a=0
	for property in properties:
		property_num=[x[0] for x in data].count(property)
		property_probably=float(property_num)/len(data)
		s=0
		for category in categories:
			property_category_num=data.count([property,category])
			property_category_probably=float(property_category_num+0.001)/float(property_num)
			s-=property_category_probably*log(property_category_probably,2)
		h_d_a+=s*property_probably
	return h_d_a	