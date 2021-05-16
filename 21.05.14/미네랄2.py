r,c=map(int,input().split())
board=[]
for i in range(r):
    board.append(list(input()))
n=int(input())
height=list(map(int,input().split()))
v=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def print_board(board):
    for i in range(r):
        for j in range(c):
            print(board[i][j],end='')
        print()
    print()
def dfs(x,y,min_num):
    
            
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #print('nx',nx,ny)
        if nx<0 or nx>r-1 or ny<0 or ny>c-1:
            continue
        if board[nx][ny]=='.' or nBoard[nx][ny]==1:
            continue
        nBoard[nx][ny]=1

        if nx==0:
            
            min_num.append(0)
            print(min_num)
        else:
            o=0
            nnx=nx-1
            if board[nnx][ny]=='.':
                print('check',nx,ny)
                while nnx<r:
                    if board[nnx][ny]=='x':
                        break
                    nnx+=1
                    o+=1
                
                min_num.append(o)
                print(min_num)
        dfs(nx,ny,min_num)
                    
                

        

def cluster_check(x,y,a,b):
    
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #print('nx',nx,ny)
        if nx<0 or nx>r-1 or ny<0 or ny>c-1:
            continue
        if board[nx][ny]=='.' or nBoard[nx][ny]==1:
            continue
        nBoard[nx][ny]=1

        if nx==a and ny==b:
            return True
        
        if cluster_check(nx,ny,a,b):
            return True
    return False
    

for rh in height:
    v+=1
    h=r-rh
    if v%2==1:
        for i in range(c):
            if board[h][i]=='.':
                continue
            break
    else:
        for i in range(c-1,-1,-1):
            if board[h][i]=='.':
                continue
            
            break
    print('h',h,i)
    board[h][i]='.'        
    cluster_candidate=[]
    cluster=[]
    for j in range(4):
        nx=h+dx[j]
        ny=i+dy[j]
        if nx<0 or nx>r-1 or ny<0 or ny>c-1:
            continue
        
        
        if board[nx][ny]=='.':
            continue
        else:
            cluster_candidate.append((nx,ny))
    if len(cluster_candidate)==2:
        nBoard=[[0 for i in range(r)]for i in range(c)]
        if (cluster_check(cluster_candidate[0][0],cluster_candidate[0][1],cluster_candidate[1][0],cluster_candidate[1][1])):
            cluster.append(cluster_candidate[0])
        else:
            cluster.append(cluster_candidate[0])
            cluster.append(cluster_candidate[1])
    elif len(cluster_candidate)==3:
        nBoard=[[0 for i in range(r)]for i in range(c)]
        if (cluster_check(cluster_candidate[0][0],cluster_candidate[0][1],cluster_candidate[1][0],cluster_candidate[1][1])):
            nBoard=[[0 for i in range(r)]for i in range(c)]
            if (cluster_check(cluster_candidate[1][0],cluster_candidate[1][1],cluster_candidate[2][0],cluster_candidate[2][1])):
                cluster.append(cluster_candidate[0])
            else:
                cluster.append(cluster_candidate[0])
                cluster.append(cluster_candidate[2])
        else:
            nBoard=[[0 for i in range(r)]for i in range(c)]
            if (cluster_check(cluster_candidate[0][0],cluster_candidate[0][1],cluster_candidate[2][0],cluster_candidate[2][1])):
                cluster.append(cluster_candidate[0])
                cluster.append(cluster_candidate[1])
            else:
                nBoard=[[0 for i in range(r)]for i in range(c)]
                if (cluster_check(cluster_candidate[1][0],cluster_candidate[1][1],cluster_candidate[2][0],cluster_candidate[2][1])):
                    cluster.append(cluster_candidate[0])
                    cluster.append(cluster_candidate[1])
                else:
                    cluster.append(cluster_candidate[0])
                    cluster.append(cluster_candidate[1])
                    cluster.append(cluster_candidate[2])
    for j in cluster:

        nBoard=[[0 for i in range(r)]for i in range(c)]
        min_num=[]
        if j[0]==c-1:
            
            min_num.append(0)
            print(min_num)
        else:
            o=0
            nnx=x-1
            if board[nnx][y]=='.':
                #print('check',nx,ny)
                while nnx<r:
                    if board[nnx][y]=='x':
                        break
                    nnx+=1
                    o+=1
                min_num.append(o)
                print(min_num,x,y)
        dfs(j[0],j[1],min_num)
        print('min',min_num)
    
    
            

                    



    

            
                
    

                
    print_board(board)
print_board(board)




                    


