n,k=map(int,input().split())
off=n-1
n*=2
belt=list(map(int,input().split()))

bRobot=[0]*n
def roll(array):
    temp=[0]*n
    
    for i in range(n-1):
        temp[i+1]=array[i]
    temp[0]=array[n-1]
    return temp

nRobot=1
num=1

while True:
    
    bRobot=roll(bRobot)
    belt=roll(belt)
    print('brobot',bRobot)
    if bRobot!=0:
        bRobot[off]=0
    nMax=10000000
    for i in range(1,n):
        if bRobot[i]!=0:
            nMax=min(nMax,bRobot[i])
    if nMax==10000000:
        nMax=0
    nMax=bRobot.index(nMax)
    temp=[0]*n
    print('f',nMax,bRobot)
    time=0
    check=True
    if bRobot[(nMax+1)%n]!=0:
        check=False
    while n>time:
        if n-1==time and check==True and bRobot[nMax]!=0:
            break

        if bRobot[nMax]!=0 and bRobot[(nMax+1)%n]==0 and nMax!=off and belt[(nMax+1)%n]!=0:
            bRobot[(nMax+1)%n]=bRobot[nMax]
            bRobot[nMax]=0
            belt[(nMax+1)%n]-=1
            print('check')
        print(nMax,bRobot)
        nMax=(nMax-1)%n
        time+=1


    print('n',bRobot)
    if belt[0]!=0 and bRobot[0]==0:
        bRobot[0]=nRobot
        nRobot+=1
        belt[0]-=1
    nZero=0
    print(num,belt,bRobot)
    for i in belt:
        if i==0:
            nZero+=1
    if nZero>=k:
        print(num)
        exit(0)
    
    input()
    num+=1



        
