import copy
n,m=map(int,input().split())
data=[]
cctv=[[],[],[],[],[],[],[]]
print(cctv)
for i in range(n):
    data.append(list(map(int,input().split())))
    for j in range(m):
        if data[i][j]!=0:
            cctv[data[i][j]].append((i,j))
i=0
result=0

def up(i):
    global result
    for j in range(i[0]-1,-1,-1):
        if data[j][i[1]]==6:
            break
        if data[j][i[1]]!=-1:
            result+=1
        data[j][i[1]]=-1
def down(i):
    global result
    for j in range(i[0]+1,n):
        if data[j][i[1]]==6:
            break
        if data[j][i[1]]!=-1:
            result+=1
        data[j][i[1]]=-1

def left(i):
    global result
    for j in range(i[1]-1,-1,-1):
        if data[i[0]][j]==6:
            break
        if data[i[0]][j]!=-1:
            result+=1
        data[i[0]][j]=-1

def right(i):
    global result
    for j in range(i[1]+1,m):
        if data[i[0]][j]==6:
            break
        if data[i[0]][j]!=-1:
            result+=1
        data[i[0]][j]=-1
for i in cctv[5]:
    left(i)
    right(i)
    up(i)
    down(i)
    
print(data)
    
for i in cctv[1]:
    

    