import copy
from itertools import combinations
n,m=map(int,input().split())
board=[]
empty=[]
wall=[]
virus=[]
for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        if board[i][j]==0:
            empty.append((i,j))
        elif board[i][j]==1:
            wall.append((i,j))
        else:
            virus.append((i,j))

def dfs(b,x,y):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    for j in range(4):
        nx=x+dx[j]
        ny=y+dy[j]
        if nx<0 or nx>n-1 or ny<0 or ny>m-1 or b[nx][ny]!=0:
            continue
        b[nx][ny]=2
        dfs(b,nx,ny)

#dfs(board,0,0)
#print(board)

nMax=0


for holls in combinations(empty,3):
    nBoard=copy.deepcopy(board)
    for holl in holls:
        nBoard[holl[0]][holl[1]]=1
    for i in virus:
        dfs(nBoard,i[0],i[1])
    num=0
    for i in range(n):
        for j in range(m):
            if nBoard[i][j]==0:
                num+=1
    
    nMax=max(nMax,num)
    
print(nMax)
        
