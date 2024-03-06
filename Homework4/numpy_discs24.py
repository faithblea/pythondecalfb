import numpy as np 
import time 

def function(num): 
    return num**2

def loop_speedtest (n): 
    start= time.time()
    result= list(range(n))
    for i in result: 
        result[i]= function(result[i])
    end = time.time()
    return end - start 

def numpy_speedtest(n): 
    start = time.time()
    result= np.arange(n)
    result = function(result)
    end= time.time()
    return end- start 
reps =1000 
# print(loop_speedtest(reps))
# print(numpy_speedtest(reps))

## 
## Find the unique elements in an array and the number of each element 
##[10,2,5,10,8,2,9,8]
##[2,5,8,9,10], [2,1,2,1,2]

myArray= np.array([10,2,5,10,8,2,9,8])
print(np.unique(myArray, return_counts= True))

## Given a 2D array, find the mean of each of the columns and replace each element less than the
##column's mean with the mean 


## ([34,37, 29], 
## [1,36,41], 
## [37,34,29], 
## [1, 49, 14])

myArray = np.array([[34,37, 29],[1,36,41],[37,34,29],[1, 49, 14]])

means= np.mean(myArray, axis=1)
#axis=0 horizontal axis rows 
#axis=1 vertical axis columns 
for i in range(myArray.shape[1]): 
    myArray[:,i][myArray[:,i]< means[i]]=means[i]

print(means)