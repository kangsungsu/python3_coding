import copy
def dfs(m,a,b,p):
    board=copy.deepcopy(m)
    board[a][b][2]=-1
    sum=board[a][b][0]
    print('sum',sum)
    pos=copy.deepcopy(p)
    pos[board[a][b][0]][0]=-1
    for i in range(4):
        print(board[i])
    print('ab',a,b)
    
    for j in range(1,17):
        
        x,y=pos[j][0],pos[j][1]
        direct=board[x][y][1]
        n=board[x][y][0]
        fish=board[x][y][2]
        #print('j',j)
        #print('xy',x,y)
        #print('d',direct)
        #print('n',n)
        #print('fish',fish)
        #for i in range(4):
            #print(board[i])
        #print('pos',pos)
        #print()
        if x==-1:
            continue
            
        while True:
            c=0
            dx=d[direct-1][0]+x
            dy=d[direct-1][1]+y
            #print('dx dy',dx,dy)
            if (dx<0 or dx>3 or dy<0 or dy>3) or board[dx][dy][2]!=1:
                if c==8:
                    break
                direct=(direct+1)%8
                board[x][y][1]=direct
                c+=1
                continue
            else:
                #print("change")
                #print()
                pos[n][0],pos[n][1],pos[board[dx][dy][0]][0],pos[board[dx][dy][0]][1]=pos[board[dx][dy][0]][0],pos[board[dx][dy][0]][1], pos[n][0],pos[n][1]
                board[x][y],board[dx][dy]=board[dx][dy],board[x][y]
                
            
                break
        
    for i in range(4):
            print(board[i])


m=[]
d=[[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
sum=0
pos=[(0,0)]*17
for i in range(4):
    
    m.append([])
    array=list(map(int,input().split()))
    for j in range(0,7,2):
        m[i].append([array[j],array[j+1],1])
        pos[array[j]]=[i,j//2]




print(dfs(m,0,0,pos))