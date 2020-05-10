from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

#plotting on our canvas
plt.plot([1,2,3],[4,5,1])

#show what we plotted
plt.show()

#input("Press Enter to continue...")

x=[5,8,10]
y=[12,16,6]

# adding labels, title to plot
plt.plot(x,y)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
#input("Press Enter to continue")

style.use('ggplot') #-> once used, used throughout the file
x2=[6,9,11]
y2=[6,15,7]
#styling ensures better looking graphs like grids, better colour contrast
plt.plot(x,y,linewidth=1)
plt.plot(x2,y2,linewidth=5)

plt.title('Epic info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
#input("Press Enter to continue")

plt.plot(x,y,'y',label='line one', linewidth=5)
plt.plot(x2,y2,'r',label="line two",linewidth=1)

plt.title("Epic info")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.legend()
plt.grid(True, color='k')
# changed grid and added labels
plt.show()

plt.bar(x, y, align='center')
plt.bar(x2,y2,color='g',align='center')

plt.show()

plt.scatter(x,y,c='y',label='x,y',s=20)
plt.scatter(x2,y2,c='b',label='x2,y2',s=30)

plt.show()

(x,y)=np.loadtxt('example.csv',unpack=True,delimiter=',')
plt.plot(x,y)
plt.title("loaded from csv")
plt.show()

style.use('fivethirtyeight')

fig=plt.figure()
#In order to modify the figure, we need to reference it, so we'll store it to 
#the variable called fig. Then we define ax1 as a subplot on the figure.
xs=[]
ys=[]
for i in range(10):
    x=i
    y=np.random.randint(10)
    xs.append(x)
    ys.append(y)

ax1 = fig.add_subplot(221)
plt.plot(xs,ys,'y',label='1', linewidth=5)
ax2 = fig.add_subplot(222)
plt.plot(xs,ys,'y',label='2', linewidth=5)
ax3 = fig.add_subplot(212)
plt.plot(xs,ys,'y',label='3', linewidth=1)
plt.show()
# A 221 means 2 tall, 2 wide, plot no 1. 222 is 2 tall,2 wide and plot no 2

#fig.savefig('(path to figure)test2png.png')
#fig.set_size_inches(18.5, 10.5)
#plt.figure(figsize=(20,10))-> incase u didn't use fig=plt.figure()

'''
The purpose of using plt.figure() is to create a figure object.

The whole figure is regarded as the figure object. It is necessary to explicitly use plt.figure() when we want to tweak the size of the figure and when we want to add multiple Axes objects in a single figure.
It's necessary to use it thought as it is explicitly created.
'''

