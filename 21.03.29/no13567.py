
n,m=map(int,input().split())
direct=2
x,y=0,0
for i in range(m):
    a,b=input().split()
    b=int(b)
    if a=='MOVE':
        if direct==0:
            x-=b
        elif direct==1:
            y-=b
        elif direct==2:
            x+=b
        else:
            y+=b
        if x<0 or x>n or y<0 or y>n:
            print(-1)
            exit(0)
        print(x,y)
    else:
        if b==0:
            direct=(direct+1)%4
        else:
            direct=(direct-1)%4
        print(direct)
print(x,y)
            


