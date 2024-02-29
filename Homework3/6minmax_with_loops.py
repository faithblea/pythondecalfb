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

list1=[-1, 45, 205, 42, 342, 56]

large=list1[0]
tiny=list1[0]



