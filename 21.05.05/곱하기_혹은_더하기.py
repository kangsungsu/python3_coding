data=list(map(int,input()))
result=data[0]
for i in range(1,len(data)):
    if result==0 or result==1:
        result+=data[i]
    else:
        result*=data[i]
print(result)
