n=int(input())
data=list(map(int,input().split()))

data.sort(reverse=True)
p=0
result=0
while True:
    if p>=n:
        break
    p+=data[p]
    
    result+=1
    print(p)
print(result)
        
