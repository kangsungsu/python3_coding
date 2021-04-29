n,x,k=map(int,input().split())
r,c,m,s,d=[],[],[],[],[]
for i in range(x):
    a,b,mN,sN,dN=map(int,input().split())
    
    r.append(a-1)
    c.append(b-1)
    
    m.append(mN)
    s.append(sN)
    d.append(dN)
temp_x=x
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

for i in range(k):
    print(i)
    temp_x=len(r)
    for j in range(temp_x):
        #print(s,temp_x)
        for y in range(s[j]):
            r[j]=(r[j]+dx[d[j]])%n
            c[j]=(c[j]+dy[d[j]])%n
    rTemp,cTemp,mTemp,sTemp,dTemp=[],[],[],[],[]
    #print(r,c)
    for j in range(n):
        for y in range(n):
            t=0
            zArray=[]
            zCheck=[]
            temp_x=len(r)       
            for z in range(temp_x):
                #print('z',z,r,c,temp_x)
                if r[z]==j and c[z]==y:
                    zCheck.append(d[z]%2)
                    zArray.append(z)
                    #print(j,y,r[z],c[z],z)

            if len(zArray)<=1:
                continue
            #print(len(zArray))
            if 0 in zCheck and 1 in zCheck:
                qDirect=False
            else:
                qDirect=True

            mSum=0
            sSum=0
            
            for z in zArray:
                mSum+=m[z]
                sSum+=s[z]
            
            for z in range(len(zArray)-1,-1,-1):
                del r[zArray[z]]
                del c[zArray[z]]
                del m[zArray[z]]
                del s[zArray[z]]
                del d[zArray[z]]
            if mSum//5==0:
                continue
            if qDirect==True:
                for z in range(4):
                    r.append(j)
                    c.append(y)
                    m.append(mSum//5)
                    s.append(sSum//len(zArray))
                    d.append(z*2)
            elif qDirect==False:
                for z in range(4):
                    if mSum//5==0:
                        continue
                    r.append(j)
                    c.append(y)
                    m.append(mSum//5)
                    s.append(sSum//len(zArray))
                    d.append(z*2+1)
            
    #for bx in range(temp_x):
        #print('x축',r[bx],'y축',c[bx],'속력',s[bx],'방향',d[bx],'무게',m[bx])
    #print()
result=0
for i in range(temp_x):
    result+=m[i]
print(result)
