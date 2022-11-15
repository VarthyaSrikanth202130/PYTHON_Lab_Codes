""" Function to return all palindromic substrings from a given string """ 

# Function to check palindrome
def ispalindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
# Function to print palindromic sub-strings            
def printallpalindrome(str):
    for i in range(0,len(str)):
        for j in range(i+1,len(str)+1):
            s = str[i : j+1]
            if(ispalindrome(s)):
                print(s)
# Giving input from user
str = str(input("Please enter the string: "))
#Calling function for output
printallpalindrome(str)