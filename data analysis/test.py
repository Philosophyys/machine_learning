from data_analysis import *
import numpy as np
import sys

(attributes,data) = getdata('F:\dataset.txt')

(mean,variance) = calculate(data,2)
print data