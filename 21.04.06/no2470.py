
n=int(input())
num=2000000000
data=list(map(int,input().split()))
data.sort()
#print(data)

start=0
end=n-1
start_c=start
end_c=end
sum=abs(data[start]+data[end])
while start<end:
    result=data[start]+data[end]
    
    if abs(result)<sum:
        start_c=start
        end_c=end
        sum=abs(result)
        if result==0:
            break
    elif result>0:
        end-=1
    else:
        start+=1
print(data[start_c],data[end_c])


