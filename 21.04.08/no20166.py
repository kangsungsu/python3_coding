def dfs(node,num,l):
    global sum
    d=[[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]
    for i in d:
        #print('i node',i,node, num)
        dx=i[0]+node[0]
        dy=i[1]+node[1]
        if dx<0:
            dx=n-1
        if dy<0:
            dy=m-1
        if dx>n-1:
            dx=0
        if dy>m-1:
            dy=0
        if board[dx][dy]==data[num]:
            #print("check")
            if l==num+1:
                sum+=1
                continue
            else:
                dfs((dx,dy),num+1,l)
        else:
            continue

n,m,k=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(input()))
sum=0
#def dfs():
for x in range(k):
    sum=0
    data=list(input())
    graph=[]
    for i in range(n):
        for j in range(m):
            if board[i][j]==data[0]:
                graph.append((i,j))
    #print('grapht',graph)
    for i in graph:
        
        dfs(i,1,len(data))

    print(sum)

