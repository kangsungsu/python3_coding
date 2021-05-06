from collections import deque
import copy
n=int(input())
graph=[[]for i in range(n+1)]
indegree=[0]*(n+1)
time=[0]*(n+1)

        

 
for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    for j in data[1:]:
        if j==-1:
            break
        indegree[i]+=1
        graph[j].append(i)

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
result=copy.deepcopy(time)
while q:
    now=q.popleft()
    for i in graph[now]:
        result[i]=result[now]+time[i]
        indegree[i]-=1

        if indegree[i]==0:
            q.append(i)

print(result)





         

 
