'''
You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Input: s = "a"
Output: true
Explanation: A single-character string is always a palindrome.
Input: s = "acbca"
Output: true
Explanation: "acbca" reads the same forwards and backwards, so it is a palindrome.

'''
s= input()
lis= s.split()
Flag=True

if s!= s[: : -1]:
    Flag= False

if Flag:
    print("true")
else:
    print("false")