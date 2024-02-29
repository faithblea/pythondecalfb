def BMI(height, weight): 
    bmi= weight/(height**2)
    return bmi 
# defined what BMI is, and set it to return that defined value 

height= 25 
weight= 30 
# gave values to varibles givne 

bmi = BMI(height, weight)
 # set bmi to be defined as the given BMI values 

print("BMI is", format(bmi))
# printed given values 

# this code used inspiration from geeksforgeeks.com, I simplifed it to answer out question, it was found at https://www.geeksforgeeks.org/program-to-calculate-bmi/