import copy
n,m=map(int,input().split())
data=list(map(int,input().split()))
check={}
for j in data:
    try: check[j]+=1
    except: check[j]=1
if m>=max(check.values()):
    print(n)
#print(check)
result=[]
for i in check:
    if check[i]>m:
        array=[]
        
        pos=([j for j in range(len(data)) if data[j]==i])
        #print(pos)
        for j in range(check[i]-m+1):
            #print('j',j)
            if j==0:
                array.append(set([k for k in range(0,pos[m])]))
            elif j==check[i]-m:
                array.append(set([k for k in range(pos[check[i]-m-1]+1,n)]))
            else:
                array.append(set([k for k in range(pos[j-1]+1,pos[j+m])]))
        result.append(array)
sum=1
#print(result)
l=[]
for i in result:
    sum*=len(i)
    l.append(len(i))

i=0
#print(i,sum,l)
r=[]
while i<sum:
    #print("check")
    am=[]
    k=i
    for j in l:
        am.append(k%j)
        k//=j
    #print(am)
    t=result[0][am[0]]
    #print(type(t))
    for o in range(1,len(l)):
        t=t&result[o][am[o]]
    
    #print(t)
    r.append(len(t))
    i+=1
#print(r)
print(max(r))
    

    