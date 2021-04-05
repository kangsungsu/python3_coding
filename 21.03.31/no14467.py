n=int(input())
data=[]
sum=0
for i in range(n):

    data.append(list(map(int,input().split())))
for i in range(n):
    if data[i][0]==0:
        continue
    for j in range(i+1,n):
        if data[i][0]==data[j][0]:
            data[j][0]=0
            if data[j][1]==1-data[i][1]:
                sum+=1
                data[i][1]=1-data[i][1]

print(sum)
                
        

