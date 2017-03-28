from data_analysis import *
import numpy as np

(attributes,data) = getdata('F:\dataset.txt')

istypes(data)

(mean,variance) = calculate(data,1)

print 'mean=%s,variance=%s'%(mean,variance)

miss_value(data, attributes)

data_balance(data,attributes)