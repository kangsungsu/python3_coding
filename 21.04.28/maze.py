import heapq

INF=int(1e9)



n,m,c=map(int,input().split())
graph=[[]for i in range(n+1)]
for _ in range(m):
    a,b,d=map(int,input().split())
    graph[a].append((b,d))

q=[]
distance=[INF]*(n+1)

heapq.heappush(q,(0,c))
distance[c]=0
print(distance)
while q:
    dist,now=heapq.heappop(q)

    if distance[now]<dist:
        continue

    for i in graph[now]:
        cost=dist+i[1]
        if cost<distance[i[0]]:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))


count=0
print(distance)