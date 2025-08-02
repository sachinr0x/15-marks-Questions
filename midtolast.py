ip_string= input()
split_list= ip_string.split()
#check split function

len_split= len(split_list)

res_lis=[]
odd_even=1

for item in split_list:
    temp=item
    temp_len= len(temp)
    if odd_even%2!=0:
        for j in temp:
            res_lis.append(j)
            break
    else:
        
        for k in temp:
            if k== temp[temp_len-1]:
                res_lis.append(k)
                break
            
    odd_even+=1

print(*res_lis, sep="")
            



    
            

    


