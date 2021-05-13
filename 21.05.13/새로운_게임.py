from collections import deque
n,k=map(int,input().split())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
lotation=[]
direction=[]
horse=[]
for i in range(n):
    horse.append([])
    for j in range(n):
        q=deque()
        horse[i].append(q)

for i in range(k):
    horse_x,horse_y,horse_direction=map(int,input().split())
    lotation.append([horse_x-1,horse_y-1])
    direction.append(horse_direction-1)
    horse[horse_x-1][horse_y-1].append(i)
dx=[0,0,-1,1]
dy=[1,-1,0,0]
#print(lotation)


num=1
while num<=1000:
    for i in range(k):
        #input()
        #print(lotation)
        #print(*horse)
        #print(i+1)
        x=lotation[i][0]
        y=lotation[i][1]
        if horse[x][y].index(i)!=0:
            continue
        nx=x+dx[direction[i]]
        ny=y+dy[direction[i]]
        #print('n',nx,ny)
        if nx<0 or nx>n-1 or ny<0 or ny>n-1:
            if direction[i]==0:
                direction[i]=1
            elif direction[i]==1:
                direction[i]=0
            elif direction[i]==2:
                direction[i]=3
            else:
                direction[i]=2
            nx=x+dx[direction[i]]
            ny=y+dy[direction[i]]
            if nx<0 or nx>n-1 or ny<0 or ny>n-1:
                continue
            
            if board[nx][ny]==1:
                for j in range(len(horse[x][y])):
                    m=horse[x][y].pop()
                    horse[nx][ny].append(m)
                    lotation[m][0]=nx
                    lotation[m][1]=ny
            
            elif board[nx][ny]==0:
                for j in range(len(horse[x][y])):
                    m=horse[x][y].popleft()
                    horse[nx][ny].append(m)
                    lotation[m][0]=nx
                    lotation[m][1]=ny
            continue
        #print('l',len(horse[x][y]))
        if board[nx][ny]==1:
            for j in range(len(horse[x][y])):
                m=horse[x][y].pop()
                horse[nx][ny].append(m)
                lotation[m][0]=nx
                lotation[m][1]=ny
        elif board[nx][ny]==0:
            for j in range(len(horse[x][y])):
                #print('j',j)
                #print('horse',horse)
                m=horse[x][y].popleft()
                #print('m',m)
                horse[nx][ny].append(m)
                lotation[m][0]=nx
                lotation[m][1]=ny
        elif board[nx][ny]==2:
            if direction[i]==0:
                direction[i]=1
            elif direction[i]==1:
                direction[i]=0
            elif direction[i]==2:
                direction[i]=3
            else:
                direction[i]=2
            nx=x+dx[direction[i]]
            ny=y+dy[direction[i]]
            if nx<0 or nx>n-1 or ny<0 or ny>n-1:
                continue
            if board[nx][ny]==1:
                for j in range(len(horse[x][y])):
                    m=horse[x][y].pop()
                    horse[nx][ny].append(m)
                    lotation[m][0]=nx
                    lotation[m][1]=ny
            elif board[nx][ny]==0:
                for j in range(len(horse[x][y])):
                    m=horse[x][y].popleft()
                    horse[nx][ny].append(m)
                    lotation[m][0]=nx
                    lotation[m][1]=ny
            continue
    breaker=False
    for i in range(n):
        #print('ll',len(horse[lotation[i][0]][lotation[i][1]]))
        if len(horse[lotation[i][0]][lotation[i][1]])>=4:
            breaker=True
            break
    if breaker:
        break
    num+=1


if num>1000:
    print(-1)
else:
    print(num)
            
            

        
        
        