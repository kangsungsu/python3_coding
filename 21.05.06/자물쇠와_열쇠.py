from collections import deque
n=int(input())
k=int(input())
apple=[]
for _ in range(k):
    a,b=map(int,input().split())
    if a==1 and b==2:
        continue
    apple.append((a,b))
move=[]
turn=[]
l=int(input())
for _ in range(l):
    a,b=input().split()
    move.append(int(a))
    turn.append(b)
time=0
time_i=0
direct=0
length=1
nx,ny=1,1
snail=deque()
snail.append((0,0))
snail.append((0,1))
#print(turn)
dx=[0,1,0,-1]
dy=[1,0,-1,0]
while True:

    time+=1
    nx+=dx[direct]
    ny+=dy[direct]

    if nx<1 or nx>n or ny<1 or ny>n or (nx,ny) in snail:
        break
    snail.append((nx,ny))
    if (nx,ny) not in apple:
        snail.popleft()
    else:
        apple.remove((nx,ny))
    if time_i>=len(move):
        continue
    elif time==move[time_i]:
        
        if turn[time_i]=='D':
            direct=(direct+1)%4
        else:
            direct=(direct-1)%4
        #print(direct)
        time_i+=1
        #print('t',time_i)
    #print(time,nx,ny)
print(time)

        
    
    

    


