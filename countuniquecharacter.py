str= input()

dictn= dict({})

for i in str:
    if i not in dictn.keys():
        dictn[i]= 1

    else:
        dictn[i]+=1 

for k,v in dictn.items():
    print(f"{k}:{v}")