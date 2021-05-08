from collections import deque
n,m,k,x=map(int,input().split())
graph=[[]for _ in range(n+1) ]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
q=deque()

q.append(x)
result=[]
distance=[-1]*(n+1)
distance[x]=0
while q:
    now=q.popleft()
    #print(done)
    for i in graph[now]:
        if distance[i]==-1:
            
            q.append(i)
            distance[i]=distance[now]+1
check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
    #print(q,result)
if check==False:
    print(-1)



