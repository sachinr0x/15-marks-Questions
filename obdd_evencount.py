n=int(input())
lis=[]
odd=0
even=0
for i in range(n):
    ip= int(input())
    lis.append(ip)


for i in lis:
    if i%2==0:
        even+=1
    else:
        odd+=1

print("No. of even elements:",even)
print("No of odd elements:",odd)
