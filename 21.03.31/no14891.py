gear=[]

for i in range(4):
    gear.append(list(map(int,input())))
#print(gear)
def rotation(n,d,to):
    #print(n,d,to)
    
    if (to==0 or to==-1) and n!=1:
        #print(0)
        if gear[n-1][6]!=gear[n-2][2]:
            #print(1,n)
            rotation(n-1,-1*d,-1)
    if (to==0 or to==1) and n!=4:
        if gear[n-1][2]!=gear[n][6]:
            rotation(n+1,-1*d,1)         
    if d==1:
        gear[n-1]=clock(gear[n-1])
    elif d==-1:
        gear[n-1]=anti_clock(gear[n-1])
    

def clock(g):
    result=[0]*8
    for i in range(7):
        result[i+1]=g[i]
    result[0]=g[7]
    
    return result

def anti_clock(g):
    result=[0]*8
    for i in range(1,8):
        result[i-1]=g[i]
    result[7]=g[0]
    return result


num=int(input())

for i in range(num):
    n,d=map(int,input().split())
    rotation(n,d,0)
    #print(1,gear)
sum=0
for i in range(len(gear)):
    if gear[i][0]==1:
        sum+=2**i
        #print(i)
print(sum)
    
    

