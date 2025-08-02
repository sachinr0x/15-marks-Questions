
"""
Question 1: Make a function check_palindrome() that takes a list of
strings as an argument. It returns the string which is a palindrome.

Input:
3
malayalam
radar
nitish

Output:
malayalam
radar
"""
def check_palindrome(lis1):
    for list_item in lis1:
        
        if list_item == list_item[: : -1]:
            print(list_item)

ip=int(input())
ar=[]

for i in range(ip):
    user_input= input()
    ar.append(user_input)

check_palindrome(ar)

       






