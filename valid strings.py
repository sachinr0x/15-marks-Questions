'''
Question 1

Write a python code to print the count of valid strings 
and invalid strings from a given list of strings

A string is considered as valid if it contains combinations
of alphabetes (in upper case or lower case) with/without 
spaces.

Define a function to check if a given string is valid or not
i.e if it contains combination of alphabetes.

This function will take string as input and return True 
if the string is valid, otherwise will return False.

Example:

Input:
4
HelloGood Morning
abcd123Fghy
India
Progoto.c

Output:
Count Of Valid String = 2
Count of Invalid String = 2
'''

validStrings=0
invalidStrings=0

def isValidString(x):
    global validStrings, invalidStrings
    if x.isalpha():
        validStrings+=1
    else:
        invalidStrings+=1

ip=int(input())
for i in range(ip):
    user_input= input()
    isValidString(user_input)

print("Count of Valid String =",validStrings)
print("Count of invalid String =",invalidStrings)



  