def numbofdigit(N):
    # this part of the code will help to establish what N, and store it for later use in the code
 
    # digit is the storage variable for N
    digit = 0
 
    # Calculate the countof digits in N
    while (N > 0):
 
        # add one to digit
        digit += 1
 
        # take the last number off of N
        N //= 10
    return digit
 
# Function to rotate the digits of N by K
def rotateNumberByK(N, K):
 
    # Stores count of digits in N this is the new 1234 number
    X = numbofdigit(N)
 
    # (K % 12345 +12345)% 12345 
    K = ((K % X) + X) % X
 
    # Stores first K digits of N, for example if K is 2 then will store the first two digits
    left_num = N // pow(10, X - K)
 
    # Remove first K digits of N, will rpevent the number from looking like 123451234, essentially N is 5 at this point
    N = N % pow(10, X - K)
 
    # Stores count of digits in left_no, this is a storage volue that we use in next line
    left = numbofdigit(left_num)
 
    # Append left_no to the right of digits of N, this allows 51234, it adds the 1234 to 5 in this step
    N = N * pow(10, left) + left_num
    print(N) # prints the number
 
# Driver Code
if __name__ == '__main__':
    N, K = 12345, 4 #stores the actual value of N and K here
 
    # Function Call
    rotateNumberByK(N, K)
 
    # This code is contributed by mohit kumar 29 on geeksforgeeks.com, much of this code is similiar, I created my own varibles and comments to try and understand the process
    # Here is the link I used: https://www.geeksforgeeks.org/rotate-digits-of-a-given-number-by-k/ 


