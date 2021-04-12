board=[]
for i in range(5):
    board.append(list(map(int,input().split())))
data=[]
for i in range(5):
    array=list(map(int,input().split()))
    for j in array:
        data.append(j)


def check():
    result=0
    
    for i in range(5):
        garo=0
        for j in range(5):
            if board[i][j]==-1:
                garo+=1
        if garo==5:
            result+=1
    for i in range(5):
        sero=0
        for j in range(5):
            if board[j][i]==-1:
                sero+=1
        if sero==5:
            result+=1
    dagak1=0
    for i in range(5):
        if board[i][i]==-1:
            dagak1+=1
    if dagak1==5:
        result+=1
    dagak2=0
    for i in range(5):
        if board[i][4-i]==-1:
            dagak2+=1
    if dagak2==5:
        result+=1
    return result

for i in range(25):
    for x in range(5):
        for y in range(5):
            if board[x][y]==data[i]:
                board[x][y]=-1
    if check()==3:
        print(i+1)
        exit(0)
    
            