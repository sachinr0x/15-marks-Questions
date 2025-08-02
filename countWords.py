 
"""
Create a function count_words() which takes a string as input and creates a dictionary with a word in the string as a key and its value as the number of times the word is repeated in the string. It should return the dictionary.
eg: “hello hi hello world hello” 
          dict={‘hello’:3,’hi’:1,’word’:1}
          Create another function max_occurance_word() which takes a string as input and returns the word which is occurring a maximum number of times in the string. Use the count_words function inside this function.

          """

def count_words(ip):
    seperate= ip.split()
    dict={}
    s= set(seperate)

    for eachitem in s:
        count=0

        count= seperate.count(eachitem)

        dict[eachitem]=count
    return dict

def max_occurance(ip):

    dictt=count_words(ip)

    l1=[]
    
    for values in dictt.values():
        l1.append(values)
    
    max1=max(l1)

    for i in dictt.keys():
        if dictt[i]== max1:
          return i
ip= input()

print(max_occurance(ip))





            



        



            
