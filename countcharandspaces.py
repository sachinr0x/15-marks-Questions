'''
Problem Statement
Write a Python program to compute the number
of spaces and characters in a given string.
Condition
Ignlore all the digits
Explanation
The total number of spaces and all the characters
excluding numbers/ digits are computed and printed.
Input
Hello This is ABCD from XYZ city
Output
No of spaces
6 and characters .
26
'''

def countCharsandSpaces(ipstring):
    chars=0
    spaces=0

    for character in ipstring:
        if character.isalpha():
            chars+=1
        elif character==" ":
            spaces+=1

    print(f"No of spaces {spaces} and characters {chars}")
        
ipstring= input()
countCharsandSpaces(ipstring)
