#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 


# In[204]:


l1= np.random.uniform(low=0,high=100,size=40)
l2= np.random.uniform(low=0,high=100,size=40)
l3=np.random.uniform(low=0,high=100,size=40)
# random data generator 
# code adopted from stack over flow from this website https://stackoverflow.com/questions/46933824/adding-an-axes-using-the-same-arguments-as-a-previous-axes 

fig,axs= plt.subplots(2)
fig.suptitle('H6 Question 1')
#adding subtitles
plt.xlabel('Position')

axs[0].plot(l1, linewidth=10,color= 'orange')
axs[0].plot(l2,linestyle = 'dashed',color= 'red')
#created two vertical subplots with the homeworks parameters
# code adopted from stack over flow from this website https://stackoverflow.com/questions/46933824/adding-an-axes-using-the-same-arguments-as-a-previous-axes
axs[1].plot(l3,linewidth=0, marker='D', color= 'm')
#normally use plt.scatter here, but this needs two postion values and here I only had one

# inspiration taken from matplotlib.com

plt.show()
#command to show the graph  


# In[97]:


import seaborn as sns 


# In[183]:


n=1 
R=8.314 
a=16.02 
b=0.114
#establishing the constant variables 

P,V= np.meshgrid(np.linspace(1, 10),np.linspace(10,30))
#establishing a colormap where P is between 1 and 10, and V is between 10 and 30 

T=((P+(a*(n*2/V**2))*(V-(n*b)))/(R*n))
#given equation for finding temperature 

plt.figure()
plt.imshow(T, cmap='winter', vmax=1.4, vmin= .3)
plt.xlabel('Pressure')
plt.ylabel('Volume')
plt.title('Temperature Based on Varying Volume and Pressure')
plt.colorbar()
plt.show
# graphing the equation over the given parameters
# I hope that incorporated vmin and vmax properly as shown with the color gradient, I think I was not supposed to add anything differently, if I was I am sorry! 


# In[98]:


from numpy import random


# In[193]:


pointsincircle= 0
#centering the circle

n1=1000
n2=10000 
n3=100000 
n4=1000000

#extablishing variing paratmers

for i in range(0,n1): 
    #if i is in range of the first parameter
    x1=random.random()
    y1=random.random()
    #produces a set of random variables
    distance1 =((x1*x1)+(y1*y1)**0.5)
    #radius establishment
    if distance1 <1: 
        pointsincircle +=1 
        #if the radius is less than 1 add one
pi1 = 4*pointsincircle/n1

#multiply the number by 4 and divide by the first parameter 
#the same comments apply to n1, n2, n3, and n4 cases 


for i in range(0,n2): 
    x2=random.random()
    y2=random.random()
    distance2 =((x2*x2)+(y2*y2)**0.5)
    if distance2 <1: 
        pointsincircle +=1 
pi2 = 4*pointsincircle/n2

for i in range(0,n3): 
    x3=random.random()
    y3=random.random()
    distance3 =((x3*x3)+(y3*y3)**0.5)
    if distance3 <1: 
        pointsincircle +=1 
pi3 = 4*pointsincircle/n3

for i in range(0,n4): 
    x4=random.random()
    y4=random.random()
    distance4 =((x4*x4+y4*y4)**0.5)
    if distance4 <1: 
        pointsincircle +=1 
pi4 = 4*pointsincircle/n4

print(pi1, pi2,pi3,pi4)
# the following code was adopted from FelixTechTips here is the link to the video that I used https://www.youtube.com/watch?v=FYQA2ozutTQ 

radius = 1.0
theta = np.linspace(0, 2 * np.pi, 10)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)
#radius of circle that was outlined, code taken inspriation from Medium, this is the link https://python.plainenglish.io/monte-carlo-simulation-with-matplotlib-animation-15c07c3376ec

plt.figure 
plt.scatter(x2, y2)
#plot only the x and y values corresponding to the N=1e4 calculation
plt.xlim(0, 5)
plt.ylim(0,5)
# axis limts of 5 
plt.show()

#graphical depiction of the points corresonpindg the N=1e4,note I worked and really tried to find a solution to why there is only 
# one point plotted, and simply could not do it, and I couldn't make any office hours, however I did find a code that had it, and commented on it 
#below to hopefully demonstrate my understanding, I just couldn't figure out how to adopt it to my calulcations


# In[192]:


import numpy as np
from numpy.random import uniform
import matplotlib.pyplot as plt

num_of_samples = 150
#establishing the number of samples

x = uniform(low=-1.0, high=1.0, size=num_of_samples)
y = uniform(low=-1.0, high=1.0, size=num_of_samples)
#samples are uniformly picked from -1 to 1 and the sample size is 150 

radius = 1.0
theta = np.linspace(0, 2 * np.pi, 1000)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)
#establishing the baseline circle with corresponding theta 
    

x_samples = x[:int(num_of_samples)]
y_samples = y[:int(num_of_samples)]
#establishing a callable variable for x and y and number of samples 

inside_circle = np.sqrt(x_samples ** 2 + y_samples ** 2) <= 1
# establishing that our new variable is now the radius

x_inside = x_samples[inside_circle]
x_outside = x_samples[~inside_circle]

y_inside = y_samples[inside_circle]
y_outside = y_samples[~inside_circle]
#establishing seperate variables for inside and outside the circle 

plt.scatter(x_inside, y_inside, 4, c='g')
# all the data inside circle is plotted and the color green 

plt.scatter(x_outside, y_outside, 4, c='m')
#all the data outside the circle is plotted and the color magenta 

plt.plot(x_circle, y_circle)
#plot both of them

plt.show
#show the the plot 

# The following was a very close adaptation taken from an animation in Medium (link here: https://python.plainenglish.io/monte-carlo-simulation-with-matplotlib-animation-15c07c3376ec)
# Since my own code was successful (trust me I really tried, and was so stuck, I am so sorry.) hopefully this establishes some of my understanding for the HW, thank you! 


# In[ ]:




