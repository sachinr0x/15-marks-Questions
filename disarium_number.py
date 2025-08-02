lbound= int(input())
ubound= int(input())

start=lbound

dis_list=[]

for i in range(lbound, ubound+1):
    str_start= str(start)
    length= len(str_start)
    sum=0

    for j in range(length):
        num= int(str_start[j])
        sum+= num**(j+1)

    if sum== start:
        dis_list.append(start)

    start+=1

print(dis_list)


    





    
