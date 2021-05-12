
n,c=map(int,input().split())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)

edges=[]
v={}
for i in range(n-1):
    for j in range(i,n):
        d=(x[i]-x[j])**2+(y[i]-y[j])**2
        if d<c:
            continue
        
        edges.append((d,i,j))
edges.sort()
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent, b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a
def find_parent(parent,node):
    if parent[node]!=node:
        return find_parent(parent,parent[node])
    return node
parent=[i for i in range(n)]
result=0
for i in edges:
    if find_parent(parent,i[1])==find_parent(parent, i[2]):
        continue
    union(parent,i[1],i[2])
    result+=i[0]
f=find_parent(parent, 0)
print(1)
fp=set(parent)
#print(fp)
if len(fp)==1:
    print(result)
else:
    print(-1)
    

        