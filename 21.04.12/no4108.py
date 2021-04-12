def count(i,j):
    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]
    if board[i][j]=='*':
        return '*'
    count=0
    for k in range(8):
        nx=i+dx[k]
        ny=j+dy[k]
        if nx<0 or ny<0 or nx>n-1 or ny>m-1:
            continue
        if board[nx][ny]=='*':
            count+=1
    return count
    
    

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    board=[]
    for i in range(n):
        board.append(list(input()))
    for i in range(n):
        for j in range(m):
            print(count(i,j),end="")
        print()

