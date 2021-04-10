import sys
n,m=map(int,sys.stdin.readline().split())

data=list(map(int,sys.stdin.readline().split()))
result=[]
ac=[]
sum=0
ac=[0]
for i in range(n):
    sum+=data[i]
    ac.append(sum)
#print(ac)
result=[]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    result.append(ac[b]-ac[a-1])
    
print(*result)