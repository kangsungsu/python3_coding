n,m,f=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
tx,ty=map(int,input().split())
tx-=1
ty-=1
passenger_x, passenger_y, destination_x,destination_y=[],[],[],[]
for _ in range(m):
    a,b,c,d=map(int,input().split())
    passenger_x.append(a-1)
    passenger_y.append(b-1)
    destination_x.append(c-1)
    destination_y.append(d-1)
distance=100
directions = (-1,0), (0,-1), (1,0), (0,1) 
def excute_road(x,y,dx,dy):
    
    count=[[-1 for _ in range(n)]for i in range(n)]
    queue=[]
    count[x][y]=0
    queue.append([x,y])
    count[x][y]=0
    while queue:
        nx,ny=queue.pop(0)
        if nx==dx and ny==dy:
            return nx,ny,count[nx][ny]
        for px, py in directions:
            nextx=nx+px
            nexty=ny+py
            if 0 <= nextx < n and 0 <= nexty < n and count[nextx][nexty] == -1 and board[nextx][nexty] != 1:
                queue.append([nextx,nexty])
                count[nextx][nexty] = count[nx][ny] + 1
        

        
#print(excute_road(tx,ty,passenger_x[0],passenger_y[0]))
temp_m=m

for j in range(m):
    sum_fuel=0
    distance=100
    for i in range(temp_m):
        
        ux,uy,temp_distance=excute_road(tx,ty,passenger_x[i],passenger_y[i])
        if temp_distance<distance:
            distance=temp_distance
            dx,dy=passenger_x[i],passenger_y[i]
            distance_number=i
                    
        elif temp_distance==distance:
            if dx>passenger_x[i]:
                dx,dy=passenger_x[i],passenger_y[i]
                distance_number=i
            elif dx==passenger_x[i]:
                if dy>passenger_y[i]:
                    dx,dy=passenger_x[i],passenger_y[i]
                    distance_number=i
    del passenger_x[distance_number]
    del passenger_y[distance_number]
    
    temp_m-=1
    tx,ty,distance2=excute_road(dx,dy,destination_x[distance_number],destination_y[distance_number])
    del destination_x[distance_number]
    del destination_y[distance_number]
    if distance+distance2>f:
        print(-1)
        exit(0)
    else:
        f-=distance+distance2
        f+=distance2*2
        #print('check')
    #print('now-fuel',f,distance,distance2,tx,ty,dx,dy,distance_number,destination_x,destination_y)
print(f)


    

                

        
     