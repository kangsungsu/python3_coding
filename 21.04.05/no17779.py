import copy
n=int(input())
a=[[0]]
result=[]
for i in range(n):
    
    a.append([0]+list(map(int,input().split())))

def gary(i,j,d1,d2):
    data=[0]*6
    bound = [[0]*(n+1) for i in range(n+1)]
    
    for x in range(d1+1):
        bound[i+x][j-x]=5
        bound[i+d2+x][j+d2-x]=5
    for x in range(d2+1):
        bound[i+x][j+x]=5
        bound[i+d1+x][j-d1+x]=5
    
    for x in range(1,i+d1):
        for y in range(1,j+1):
            if bound[x][y]==5:
                break
            bound[x][y]=1
    for x in range(1,i+d2+1):
        for y in range(n,j,-1):
            if bound[x][y]==5:
                break
            bound[x][y]=2
    for x in range(i+d1,n+1):
        for y in range(1,j-d1+d2):
            if bound[x][y]==5:
                break
            bound[x][y]=3
    for x in range(n,i+d2,-1):
        for y in range(n,j-d1+d2-1,-1):
            if bound[x][y]==5:
                break
            bound[x][y]=4
    for x in range(1,n+1):
        for y in range(1,n+1):
            data[bound[x][y]]+=a[x][y]
    data[5]+=data[0]
    
    return max(data)-min(data[1:])
            
            


  

for i in range(1,n+1):
    for j in range(1,n+1):
        d1,d2=1,1
        while j-d1>=1 and i+d1+d2<=n:
            while j+d2<=n and i+d1+d2<=n:
                #print(i,j,d1,d2)
                result.append(gary(i,j,d1,d2))
                d2+=1
            d1+=1
            d2=1
            

print(min(result))