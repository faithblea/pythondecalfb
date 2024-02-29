word1 = "UC Berkeley"
# estrablishing the string variable 
vowels = "aeiouAEIOU"
#establishing the vowels that I want the function to look out for
 
count = sum(word1.count(vowel) for vowel in vowels)
#asking it to add all the vowels found in string for how many vowels there are in vowels

print(count)
#print the count function

# this code was inpired by geekforgeeks, I chagned the varibles as well as added comments to better my understanding
# the website that I found it on was  https://www.geeksforgeeks.org/python-program-count-number-vowels-using-sets-given-string/