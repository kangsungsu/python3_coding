def solution(n, build_frame):
    answer = [[]]
    board=[[-1 for i in range(n+1)] for i in range(n+1)]
    print(board)
    for x,y,a,b in build_frame:
        if b==1:
            if a==0:

                if y!=0:
                    #print(x,y)
                    if board[x][y-1]!=0:
                        continue
                if x!=0:
                    if board[x-1][y]!=1:
                        continue
                borad[x][y]=0
            if a==1:
                
                if (board[x][y-1]!=0 and board[x+1][y-1]!=0) and (board[x-1][y]!=1 or board[x+1]!=1):
                    continue
                board[x][y]=1
        else:
            if a==0:
                
                if board[x][y+1]==0:
                    continue
                if x>=1:
                    
                    if board[x-1][y]==0:
                        continue
                    if x>=2:
                        if not (board[x-2][y+1]==1 and board[x][y+1]):
                            continue
                if x<=n-1:
                    if board[x]
                



                
                
    return answer
solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])