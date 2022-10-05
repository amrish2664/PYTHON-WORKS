
def prime(n):
    count=0
    for y in range(2,n+1):
        if(n%y==0):
            count+=1
    if(count==1):
        return 1
    else:
        return 0   
x=int(input("enter number:"))
i=2
lst=[]
while(1):
    if(prime(i)):
        lst.append(i)
        if(len(lst)==x):
            break
    i=i+1
print(*lst)    
    
