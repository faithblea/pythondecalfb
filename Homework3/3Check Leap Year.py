
def leap_year(year): #establishing my initial function 
    
    leap= False
    # the leap year is false until proven other wise
    if (year % 400==0): 
        leap= True 
    # if the year is divisible by 400 then it is true
    elif (year %100 ==0): 
        leap= False
    # if the year is divisible by 100 then it is false 
    elif (year %4 == 0): 
        leap= True
    # if the year is divisible by 4 then it is true 
    return leap

year= 2020 # input for the year 
print (leap_year(year))
# print whether it was true or false
# this code was inspired by stackoverflow, here is the link that I used https://stackoverflow.com/questions/56502898/how-do-i-solve-the-leap-year-function-in-python-for-hackerrank