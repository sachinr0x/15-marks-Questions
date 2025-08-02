word = input()
w2= word.replace(" ", "") 
vowels  = 'aeiouAEIOU'
v = 0
c = 0
for i in w2:
    if i in vowels:
        v += -1
    if i not in vowels:
        c += 1
x = v + c
print (x)
          


    
