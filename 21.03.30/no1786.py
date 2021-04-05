t=list(input())
p=list(input())
true=0

sum=0
list=[]

bulb=[1]
l=1
i,j=1,0
while i<len(p):
    while j<len(p)-1:
        if len(bulb)==len(p):
            break
        if p[i]==p[j]:
            l+=1
            bulb.append(l)
            i+=1
            j+=1
            #print(i,j,l)
        else:
            l=0
            bulb.append(l)
            i+=1
            j=0
            #print(i,j,l)
            break

i,j=0,0

n=len(t)
m=len(p)
while n-m>=i:
    #print(i,i+j,j)
    if j<m and t[i+j]==p[j]:
        j+=1
        if j==m:
            list.append(i+1)
            i+=1
            j=0

    
    else:
        if j==0:
            i+=1
        else:
            i+=j-bulb[j-1]
            j=bulb[j-1]


print(len(list))
print(*list)

        


        

