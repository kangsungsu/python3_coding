from collections import deque
n,g=map(int,input().split())
board=[[] for _ in range(n+1)]

#print(board)
for _ in range(n-1):
    p,q,r=map(int,input().split())
    board[p].append((q,r))
    board[q].append((p,r))

def bfs(board,start,visited,distance):
    queue=deque()
    queue.append((start))
    #distance[start]=0
    visited[start]=True
    while queue:
        a=queue.popleft()
        
        for i in board[a]:
            #print(i)
            if not visited[i[0]]:
                queue.append(i[0])
                distance[i[0]]=min(min(distance[i[0]],i[1]),distance[a])
                visited[i[0]]=True
    return distance

for i in range(g):
    k,v=map(int,input().split())
    visited=[False for _ in range(n+1)]
    distance=[1000000000 for _ in range(n+1)]
    
    distance=bfs(board,v,visited,distance)
    count=0
    for j in distance:
        if j==1000000000 or j<k:
            continue
        count+=1
    print(count)
    #print('m',i,q)
        
