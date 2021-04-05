n,l=map(int,input().split())
arr=[]
result=0
sum=0

def road(data):
    global sum
    flag=[0]*n
    
    for i in range(n-1):
        if data[i]==data[i+1]:
            continue
        elif abs(data[i]-data[i+1])>1:
            #print(i,1)
            return
        elif data[i]+1==data[i+1]:
            for j in range(l):
                if i-j<0:
                    #print(i,2)
                    return
                if data[i-j]!=data[i]:
                    #print(i,3)
                    return
                if flag[i-j]==1:
                    #print(i,4)
                    return
                flag[i-j]=1
        elif data[i]-1==data[i+1]:
            for j in range(l):
                if i+j+1>n-1:
                    #print(i,5)
                    return
                if data[i+1]!=data[i+1+j]:
                    #print(i,j,6)
                    return
                flag[i+j+1]=1
    
    sum+=1

for i in range(n):
    arr.append(list(map(int,input().split())))
new_arr = list(map(list, zip(*arr)))

for i in range(n):
    road(arr[i])
for i in range(n):
    road(new_arr[i])
print(sum)

                
                




