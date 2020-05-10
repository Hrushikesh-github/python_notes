import pandas as pd
import numpy as np

############creating series################
ser1=pd.Series([1.5,2.5,3,4.5,5,6])
# 1st column represents index of the Series
code=["IND","CAN","GER","AUS","SWI","USA"]
ser2=pd.Series(["India","Canada","Germany","Aussie","Swiss","America"],
        name="Countries",index=code)
ser3=pd.Series(["A"]*4)
ser4=pd.Series({"India":"New Delhi","USA":"Washington","UK":"London"})
print(ser1)
print(ser2)
print(ser3)
print(ser4)

ser5=pd.Series(np.linspace(1,10,5))
#Return evenly spaced numbers over a specified interval.
ser6=pd.Series(np.random.normal(size=5))
print(ser5)
print(ser6)

#####################################################################
######TAKING VALUES################

print(ser4.values)
print(ser4.index)
'''
['New Delhi' 'Washington' 'London']
Index(['India', 'USA', 'UK'], dtype='object')
'''
print("\n")
print(ser6.values)
print(ser6.index)
'''
[ 0.28384767 -1.07273912  0.00320795  0.86446963 -1.62336104]
RangeIndex(start=0, stop=5, step=1)
'''

print(len(ser2))
print(ser2.shape)
print(ser2.size)

num = [000, 100, 200, 300, 400, 500, 600, 700, 800, 900]

idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

series = pd.Series(num, index=idx)

print(series)

# syntax of start:end:step, the segments representing the first item, last item, and the increment between each item that you would like as the step

print("\n [2:4] \n")
print(series[2:4])

print("\n [1:6:2] \n")
print(series[1:6:2])

print("\n [:6] \n")
print(series[:6])

print("\n [4:] \n")
print(series[4:])

print("\n [:4:2] \n")
print(series[:4:2])

print("\n [4::2] \n")
print(series[4::2])

print("\n [::-1] \n")
print(series[::-1])# -> reverses the series

print("------Take()-------")
print(ser2.take([2,4,1])) #-> like to ser2.head() & ser2.tail(2)


