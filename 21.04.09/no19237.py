n,m,k=map(int,input().split())
board=[]
out=0
for i in range(n):
    board.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
direction=list(map(int,input().split()))
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)
print(priorities)
smell_shark=[]
for i in range(n):
    smell_shark.append([])
    for j in range(n):
        
        smell_shark[i].append(0)
smell_remain=[]
for i in range(n):
    smell_remain.append([])
    for j in range(n):
        
        smell_remain[i].append(0)

pos_x=[0]*(m+1)
pos_y=[0]*(m+1)
for i in range(n):
    for j in range(n):
        if board[i][j]!=0:
            pos_x[board[i][j]]=i
            pos_y[board[i][j]]=j
print(pos_x,pos_y)

def update():
    global pos_x
    global pos_y
    global smell_shark
    global smell_remain
    global out
    for i in range(1,m):
        for j in range(i+1,m+1):
            if pos_x[i]==pos_x[j] and pos_y[i]==pos_y[j] and pos_x[i]!=-1:
                pos_x[j],pos_y[j]=-1,-1
                direction[j-1]=0
                out+=1
    for i in range(n):
        for j in range(n):
            if smell_remain[i][j]!=0:
                smell_remain[i][j]-=1
                if smell_remain[i][j]==0:
                    smell_shark[i][j]=0
    for i in range(1,m+1):
        if pos_x[i]<0:
            continue
        smell_remain[pos_x[i]][pos_y[i]]=k
        smell_shark[pos_x[i]][pos_y[i]]=i
    

def go():
    global pos_x
    global pos_y
    global smell_shark
    global smell_remain
    global direction
    print()
    for i in range(1,m+1):
        nxmy=-1
        nymy=-1
        direction_my=0
        for j in range(4):
            #print(i,j)
            #print(direction[i-1])
            #print(priorities[i-1][direction[i-1]-1][j])
            #print(dx[priorities[i-1][direction[i-1]][j]])
            nx=pos_x[i]+dx[priorities[i-1][direction[i-1]-1][j]-1]
            ny=pos_y[i]+dy[priorities[i-1][direction[i-1]-1][j]-1]
            if i==2:
                print(nx,ny,nxmy,nymy)
            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            if smell_shark[nx][ny]==i and nxmy==-1 and nymy==-1:
                nxmy=nx
                nymy=ny
                direction_my=priorities[i-1][direction[i-1]-1][j]
            if smell_remain[nx][ny]==0:
                pos_x[i]=nx
                pos_y[i]=ny
                #print("nx, ny",nx,ny)
                direction[i-1]=priorities[i-1][direction[i-1]-1][j]
                break
            if j==3:
                pos_x[i]=nxmy
                pos_y[i]=nymy
                direction[i-1]=direction_my
                
            
            

        
    

update()
num=0
while out!=m-1:
    print(out)
    go()
    update()
    num+=1
#for i in range(8):
#    go()
#    update()


for i in range(n):
    print()
    for j in range(n):
        print(smell_remain[i][j],end=" ")
print()
for i in range(n):
    print()
    for j in range(n):
        print(smell_shark[i][j],end=" ")
print()
print(pos_x)
print(pos_y)
print(direction)
print(out)
print(num)
        