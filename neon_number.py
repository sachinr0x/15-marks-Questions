
lbound= int(input())
ubound= int(input())
start= lbound
neon_list=[]

for i in range(lbound, ubound+1):
    start_sqr= start*start
    start_sqr_string= str(start_sqr)
    len_string= len(start_sqr_string)
    final_sum=0

    for j in range (len_string):
        final_sum+=int(start_sqr_string[j])

    if final_sum== start:
        neon_list.append(start)
    start+=1


if neon_list==[]:
    print("No neon numbers present in a given range")
else:
    print(neon_list)



