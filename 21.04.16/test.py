import copy
n,m=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
new_board=copy.deepcopy(board)
for i in range(1,n):
    for j in range(m):
        sum=0
        if j==0:
            new_board[i][j]+=board[i-1][j]
        else:
            new_board[i][j]=board[i][j]+board[i-1][j-1]+board[i-1][j]+board[i][j-1]
            if new_board[i][j]==4:
                k=1
                while True:
                    if i-k<0 or j-k<0:
                        break
                    if new_board[i][j]!=4:
                        break
                    breaker=True
                    for l in range(1,k+1):
                        if new_board[i-k+l][j-k]!=4:
                            breaker=False
                            break
                    for l in range(1,k+1):
                        if new_board[i-k][j-k+l]!=4:
                            breaker=False
                            break 
                    if breaker=False:
                        break
                    

                
            
        

    
    
    
print(add(3,1,2))   