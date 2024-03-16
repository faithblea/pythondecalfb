import numpy as np
#initalized command to run numpy

#Part 1 
arr = np.array([[1,1,1], [1,2,3], [2,2,2]])
#intial set up to run array 

same = [True, True, True]
#establishing that they are all equal 
for t in range(len(arr)): 
    for j in range(len(arr[t])):
        #nested for loop to examine the elements in the entire array
        prev = arr[t][0]
        #looking at the first row and all of the columns in that row 
        if arr[t][j] != prev: 
            same[t] = False
        # if there is another row outside of this first one ignore it 
for t in range(len(arr)):
    if same[t]:
        print(arr[t])
        #if the row t we are looking at is all equal print it 
# my CS friend helped me again with this, and helped me better understand the for loops better


# Part 2 
x= np.ones((8,8), dtype=int)
#creates an 8 by 8 grid with the data type being an integer, a grid filled by ones
x[::2, 1::2]=0
#controls the first one and every other one, alternates between 0 and 1, inserts a zero every other
x[1::2, ::2]=0
#controls the second one and every other one, alternates between 0 and 1, inserts a zero every other
print(x)
# prints the statement 
#this code was inspired by w3resource.come link is here: https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-10.php  

#Part 3 
a=np.array(['python', 'is', 'cool!'])
#initial array 
y=np.char.join(" ", a)
#inserting a space using the numpy command, and following with the name of the array 
print(y)
#printing the new array 
# this code was inspired from geeksforgeeks.com link is here: https://www.geeksforgeeks.org/how-to-insert-a-space-between-characters-of-all-the-elements-of-a-given-numpy-array/

#Part 4 
np.random.seed(12345)
#esxits to support other code 
r=np.random.randint(1,50, (4,5))
#create an array of random numbers 1-50, in a 4 column 5 row matrix
r.sort(axis=0)
#sort r by the column (0 axis is the column)
print(r)
#print r

