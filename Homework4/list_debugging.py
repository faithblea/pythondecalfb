#Part 2 
def listofnum(r1,r2): 
    return [item for item in range(r1, r2)]
#calling the function, and then telling the function to output every number within range of r1 and r2
r1, r2 = 0, 50 
#defining what r1 and r2 equal too 

print(listofnum(r1, r2))
# this calls the function for printing, used the following website for inspiration 
# https://www.geeksforgeeks.org/python-create-list-of-numbers-with-given-range/


lis= listofnum(r1, r2)
#renaming the list so that it more easily callable 

def square(lis): 
    return [i**2 for i in lis]
# for every value of the list square it 
# I encountered an error here saying i did not define my list so I created lis= listofnum(r1, r2)
print(square(lis))
#print this function

# inspriation for this code was taken from stack overflow here is the link that I used: https://stackoverflow.com/questions/12555443/squaring-all-elements-in-a-list

def newlist1(r3, r4): 
    return[item for item in range(r3, r4)]
# return an list of numbers with in the range of r3 and r4 
r3, r4= 0, 11 
#giving values to r3 and r4 

def newlist2(r5,r6): 
    return[item for item in range(r5, r6)]
# return a list or numbers with in range of r5 and r6 
r5, r6 = 19, 31 
#giving values for r5 and r6 
# no errors here :) same procedure as above 

newlist3= newlist1(r3,r4)+ newlist2(r5, r6)
del newlist3[::2]
#tells to you delete every other number
#at first I encounter the wrong deletions like 2,4,6 instead of 3,5,7 but I chnaged my ranged to fit it 
print(newlist3)
# created a new list with all of the numbers combined 


#Part 3 
rows= 5 
cols= 5 
#establishing how many numbers I want per column and row
i=0
j=0
#each of these values will start at 0 
numgrid = [[i+1+cols*j for i in range(cols)] for j in range(rows)]
#for every value in the row add one, and make sure to continue this function on to the next row in the column
for row in numgrid: 
    print(row)
#print the 2d matrix 
# this code used inspiration from stackoverflow 
#here is the link that I used: https://stackoverflow.com/questions/57864462/create-a-5-x-5-matrix-using-nested-list-comprehensions 


for t in range(len(numgrid)): 
        for j in range(len(numgrid[t])):
            #check all the numbers in the array 
            if numgrid[t][j] % 3 == 0:
                numgrid[t][j]= "?"
            # if any of these numbers are divisible by 3 put a ? there

print(numgrid)
    # look at every t in numgrid within the length of the range of numgrid
 
        # if there is a value in numgrid that is a factor of three in the colums 
# my most favoritest CS friend helped me fully understand it :) 
     
        

#Part 4 
def rem(lis1): 
    #defining rem to be a subset of lis1 
    final_list=[]
    # final list will be in list form 
    for num in lis1: 
        if num not in final_list: 
            final_list.append(num)
            #remove the numbers that are in duplicates in lis1 
    return final_list
#reuturn the finalized list 

lis1=[1,1,1,1,3,3,4,4,7]
# orignal list values

print(rem(lis1))
#print the finalized list 
#recieved an error message here saying that dup was not defined
#reliazed that I had not defined it and changed dup to be lis1 (this worked) https://www.geeksforgeeks.org/python-remove-duplicates-list/
#this code took inspiration from geeksforgeeks.com; here is the link that I used 