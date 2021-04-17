import copy


num=int(input())
up,down,front,back,left,right=[],[],[],[],[],[]
for i in range(3):
    up.append([])
    down.append([])
    front.append([])
    back.append([])
    left.append([])
    right.append([])
    for j in range(3):
        up[i].append('w')
        down[i].append('y')
        front[i].append('r')
        back[i].append('o')
        left[i].append('g')
        right[i].append('b')

def roll(up,down,front,back,left,right,d):
    front=rotate(front,d)
    cup,cdown,cfront,cback,cleft,cright=copy.deepcopy(up),copy.deepcopy(down),copy.deepcopy(front),copy.deepcopy(back),copy.deepcopy(left),copy.deepcopy(right)
    if d==True:
        
        for i in range(3):
            cright[i][0],cdown[2][i],cleft[i][2],cup[2][i]=up[2][i],right[i][0],down[2][2-i],left[2-i][2]
    else:
        for i in range(3):
            cright[i][0],cup[2][i],cleft[i][2],cdown[2][i]=down[2][i],right[i][0],up[2][2-i],left[i][2-i]
    print(cup,cdown,cfront,cback,cleft,cright,sep="\n")
    print()
    return cup,cdown,cfront,cback,cleft,cright


def rotate(board,d):
    m=copy.deepcopy(board)
    if d==True:
        
        for i in range(3):
            for j in range(3):
                m[i][j]=board[2-j][i]
        
    elif d==False:
        for i in range(3):
            for j in range(3):
                m[i][j]=board[j][2-i]
    return m

#print(front)
#roll(up,down,front,back,left,right,True)
for i in range(num):
    n=int(input())
    data=list(input().split())
    #print(data)
    cup,cdown,cfront,cback,cleft,cright=copy.deepcopy(up),copy.deepcopy(down),copy.deepcopy(front),copy.deepcopy(back),copy.deepcopy(left),copy.deepcopy(right)
    rup,rdown,rfront,rback,rleft,rright=copy.deepcopy(up),copy.deepcopy(down),copy.deepcopy(front),copy.deepcopy(back),copy.deepcopy(left),copy.deepcopy(right)
    #print(rup,rdown)
    for j in data:
        
        cup,cdown,cfront,cback,cleft,cright=copy.deepcopy(rup),copy.deepcopy(rdown),copy.deepcopy(rfront),copy.deepcopy(rback),copy.deepcopy(rleft),copy.deepcopy(rright)
        if j=='F+':
            rfront=rotate(rfront,True)
            for k in range(3):
                rright[k][0],rdown[2][k],rleft[k][2],rup[2][k]=cup[2][k],cright[k][0],cdown[2][2-k],cleft[2-k][2]
                #print(rup)
        elif j=='F-':
            rfront=rotate(rfront,False)
            for k in range(3):
                rright[k][0],rup[2][k],rleft[k][2],rdown[2][k]=cdown[2][k],cright[k][0],cup[2][2-k],cleft[2-k][2]
                

        elif j=='B+':
            rback=rotate(rback,True)
            for k in range(3):
                rright[k][2]=cdown[0][k]
                rdown[0][k]=cleft[2-k][0]
                rleft[2-k][0]=cup[0][k]
                rup[0][k]=cright[k][2]
                #print(cright)
        elif j=='B-':
            rback=rotate(rback,False)
            for k in range(3):
                rright[k][2]=cup[0][k]
                rdown[0][k]=cright[k][2]
                rleft[k][0]=cdown[0][k]
                rup[0][k]=cleft[k][0]
            
        elif j=='U+':
            rup=rotate(rup,True)
            for k in range(3):
                rright[0][k]=cback[0][k]
                rfront[0][k]=cright[0][k]
                rleft[0][k]=cfront[0][k]
                rback[0][k]=cleft[0][k]
        elif j=='U-':
            rup=rotate(rup,False)
            for k in range(3):
                rright[0][k]=cfront[0][k]
                rfront[0][k]=cleft[0][k]
                rleft[0][k]=cback[0][k]
                rback[0][k]=cright[0][k]

                
        elif j=='D+':
            down=rotate(down,True)
            for k in range(3):
                rright[2][k]=cfront[2][k]
                rback[2][k]=cright[2][k]
                rleft[2][k]=cback[2][k]
                rfront[2][k]=cleft[2][k]

        elif j=='D-':
            rdown=rotate(rdown,False)
            for k in range(3):
                rright[2][k]=cback[2][k]
                rback[2][k]=cleft[2][k]
                rleft[2][k]=cfront[2][k]
                rfront[2][k]=cright[2][k]
        elif j=='L+':
            rleft=rotate(rleft,True)
            for k in range(3):
                rup[k][0]=cback[2-k][2]
                rback[k][2]=cdown[k][2]
                rdown[k][2]=cfront[2-k][0]
                rfront[k][0]=cup[k][0]
        elif j=='L-':
            rleft=rotate(rleft,False)
            for k in range(3):
                rup[k][0]=cfront[k][0]
                rback[k][2]=cup[2-k][0]
                rdown[k][2]=cback[k][2]
                rfront[k][0]=cdown[2-k][2]
                

        elif j=='R+':
            rright=rotate(rright,True)
            for k in range(3):
                rup[k][2]=cfront[k][2]
                rback[k][0]=cup[k-2][2]
                rdown[k][0]=cback[k][0]
                rfront[k][2]=cdown[2-k][0]
        elif j=='R-':
            rright=rotate(rright,False)
            for k in range(3):
                rup[k][2]=cback[2-k][0]
                rback[k][0]=cdown[k][0]
                rdown[k][0]=cfront[k-2][2]
                rfront[k][2]=cup[k][2]
        #print(cup,cdown,cfront,cback,cleft,cright,sep="\n")
        #print()
    for x in range(3):
        for y in range(3):
            print(rup[x][y],end="")
        print()
    
    