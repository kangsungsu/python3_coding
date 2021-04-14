import queue
n=int(input())
point=[[0]*101 for _ in range(101)]
#square=[[0]*10 for _ in range(10)]
#print(point)
for i in range(n):
    x,y,d,g=map(int,input().split())
    point[y][x]=1
    add=[]
    if d==0:
        nx=x+1
        ny=y
        add.append((1,0))
    elif d==1:
        nx=x
        ny=y-1
        add.append((0,-1))
    elif d==2:
        nx=x-1
        ny=y
        add.append((-1,0))
    else:
        nx=x
        ny=y+1
        add.append((0,1))
    point[ny][nx]=1
    for j in range(1,g+1):
        for k in range(len(add)-1,-1,-1):
            add.append((add[k][1],-1*add[k][0]))
            nx+=add[k][1]
            ny+=-1*add[k][0]
            point[ny][nx]=1



result=0
for i in range(100):
    for j in range(100):
        if point[i][j]==1 and point[i+1][j+1] and point[i][j+1]==1 and point[i+1][j]==1:
            result+=1
print(result)

    