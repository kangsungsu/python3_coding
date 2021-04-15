import itertools
import copy
lo_ch=[]
lo_ho=[]
n,m=map(int,input().split())
board=[]


for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(n):
        if board[i][j]==1:
            lo_ho.append((i,j))
        if board[i][j]==2:
            lo_ch.append((i,j))
result=[]
for i in itertools.combinations(lo_ch,len(lo_ch)-m):
    ch=copy.deepcopy(lo_ch)
    b=copy.deepcopy(board)
    for j in i:
        ch.remove((j[0],j[1]))
        b[j[0]][j[1]]=0
    s=0
    for j in lo_ho:
        d=100
        for k in ch:
            d=min(d,abs(j[0]-k[0])+abs(j[1]-k[1]))
        s=s+d
    result.append(s)
print(min(result))


    

        
