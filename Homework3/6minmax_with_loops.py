l=[1,68, 105, 342, 42, 56] #given list to call from

big=l[0]
small=l[0] #initalizing these both as starting from 0, and looking at whole list

for num in l: 
    if num > big: 
        # if the number is greater than big then it is the max
        big =num 
    if num < small:
        # if the number is smaller than small  
        small = num 

print('Max',big)
print('Min',small) 

list1=[-2, 45, 205, 42, 342, 56] # orignal list

large=list1[0]
tiny=list1[0]
#initalizing list 

while tiny< -1:
    # went to office hours, tried my best to get the syntax here but ultamtely it would just print the min and max without break 
    # attempted to fix using this website https://www.w3schools.com/python/python_while_loops.asp
    print('Min', tiny)
    # while tiny was less than the smallesr number print 'Min' 
    if (tiny==0): 
     break 
    # attempt to only get on loop to print   


while large>342:
    print ('Max',large)
    # if large was greater than the maximum number then print Max 
    if (large==0): 
        break
    #again I was unsucessful with the breaks, I am sorry 
    




