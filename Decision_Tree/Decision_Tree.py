from entropy import *
# class tree_node():
# 	"""docstring for tree_node"""
# 	def __init__(self, category=None,property=None,index=None,norm=None):
# 		self.category = category
# 		self.property = property
# 		self.index = index
# 		self.norm = norm
# 		self.subnode = [ ]

# class decision_tree():
# 	"""docstring for decision_tree"""
# 	def __init__(self):
# 		#super(decision_tree, self).__init__()
# 		self.parent = tree_node()

# 	def __add_subnode(parent,property,index,norm,category=None):
# 		parent.subnode.append(tree_node(category,property,index,norm))
# 		return parent.subnode[-1]
	
# 	def train(parent,train_data,tpye='C4.5'):
# 		property=''
# 		index_=0
# 		print parent.index
# 		if ([train_data[-1][i]==train_data[-1][i] for i in (len(train_data[-1])-1)].conut(True))==(len(train_data[-1])-1):
# 			parent.category=train_data[-1][0]
# 		elif len(train_data)==1:
# 			properties=list(set([x[-1] for x in train_data]))
# 			D=dict(zip([train_data[-1].count(x) for x in properties],properties))
# 			parent.category=D[max(D)]
# 		else:
# 			(property,norm,index)=__select_property(data,tpyes=type)
# 			for x in xrange(1,10):
# 				pass
# 				parent_=__add_subnode(parent,property,index,norm,)
# 				slice_data=__slice_data(train_data,index)
# 				return(train(parent_,slice_data))

# 	def __select_property(self,train_data,types='C4.5'):
# 		max_norm=0
# 		max_property=''
# 		max_index=0
# 		norm=0
# 		index=0
# 		property=None
# 		if types=='C4.5':
# 			for i in len(data[0])-1:
# 				data=[[x[i],x[-1]] for x in train_data]
# 				if type_is(train_data[0][0])=='isfloat':
# 					(property,norm)=Select_Threshold(data)
# 					index=i
# 				else:
# 					property=i
# 					norm=Information_Gain_Ratio(data)
# 					index=i
# 				if norm >= max_norm:
# 					max_norm=standard
# 					max_property=property
# 					max_index=index
# 				else:
# 					pass
# 		elif types=='ID3':
# 			pass
# 		elif types=='CART':
# 			pass
# 		else:
# 			raise AttributeError
# 		return (max_property,max_norm,max_index)

# 	def __slice_data(train_data,index):
# 		del train_data[index]
# 		return train_data

# 	def pruning(self):
# 		pass

# 	def plot(self):
# 		pass

# 	def test(self):
# 		pass

# 	def type_is(x):
# 		try:
# 			x=float(x)
# 			return 'isfloat'
# 		except  ValueError:
# 			return 'isstr'


def train(test_data):
	result = {}
	for i in range(len(test_data[0])-1):
		data = [[x[i],x[-1]] for x in test_data]
		result[i]=Select_Threshold(data)
	fore_values[0] = result[0]
	# for x in result:
	# 	if x.values[1] >= fore_values.values[1] :
	# 		fore_values = x.values
	print fore_values
	#print R
	#print result