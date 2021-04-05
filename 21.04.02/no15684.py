n,m,h=map(int,input().split())
board=[[0 for _ in range(n+1)]for _ in range(h+1) ]
l=[]
for i in range(m):
    a,b=map(int,input().split())
    board[a][b]=1
for i in range(1,h+1):
    for j in range(1,N):
        if board[i][j]==0 and board[i][j-1]== 0 and lines[i][j+1]==0:
            l.append((i,j))


def solve(added,num):
    global num
    if added>=num:
        return
    if check():
        

#for i in range(m):
