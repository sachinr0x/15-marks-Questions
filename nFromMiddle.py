
str1= input("enter the string")
n1= int(input())


middle= len(str1)//2
    


if (len(str1[middle: middle+n1])==n1):
    print(str1[middle:middle+n1])

else:
    print(str1[middle:])

        


