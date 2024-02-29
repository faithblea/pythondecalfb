def sumtime(n): #establishes n as variable to be manipulated
    sum =0 # sum starts at 0
    while (n !=0): #when n is not equal to 0 
        sum =sum+ int(n% 10) # sum is equal to sum plus the last number in the sequence this is done for the whole number so that that they are all added together
        n= int(n/10) # divide n by 10 
    return sum 
if __name__ == "__main__": 
    n=12344 # numerical value for n 
   
    print(sumtime(n)) #printing the function that is finidng the sum of all the numbers
# I used inspiration from geeksforgeeks in this code, I changed the varaibles as well as wrote my own comments for extended understanding
# this is the link that I used https://www.geeksforgeeks.org/program-for-sum-of-the-digits-of-a-given-number/ 