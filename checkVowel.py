"""
  GIVEN some strings in that we need to print the strings which does
  not contain more than one vowels in it

  take list of strings as input and create a function vowelString()
  that will return list of strings where strings have one or no vowels in it.

input-

3
aeroplane
cfm
art

output-

cfm(no vowel)
art(one vowel)
"""
def vowelString(str1):
    lis2=[]
    vowels='aeiouAEIOU'

    for item in str1:
        count=0

        for parse_item in item:
            if parse_item in vowels:
                count+=1
            
        if count==1:
          lis2.append(f"{item}(one vowel)")
        elif count==0:
          lis2.append(f"{item}(no vowel)")
    return lis2
        
ar=[]

for i in range(int(input())):
    user_input= input()
    ar.append(user_input)

result=vowelString(ar)

for item in result:
    print(item)