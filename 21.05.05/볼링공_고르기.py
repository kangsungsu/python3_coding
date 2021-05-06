n,m=map(int,input().split())
data=list(map(int,input().split()))
result=n*(n-1)//2
for i in range(1,m+1):
    x=data.count(i)
    if x>=2:
        result-=x*(x-1)//2
print(result)