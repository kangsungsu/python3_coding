data=list(map(int,input()))
i=1
standard=data[0]
result=[0,0]
result[standard]+=1
while i<len(data):
    if data[i]!=standard:
        result[data[i]]+=1
        standard=data[i]
    i+=1
    
        
    
print(min(result))
        

    