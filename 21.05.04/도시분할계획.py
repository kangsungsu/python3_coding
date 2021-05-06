n,m=map(int,input().split())

graph=[]
for i in range(m):
    a,b,c=map(int,input().split())
    graph.append((c,a,b))

graph.sort()
parent=[i for i in range(n+1)]
def find_parent(x):
    if parent[x]!=x:
        return find_parent(parent[x])
    return x
result=0
for edge in graph:
    cost,a,b=edge
    ar,br=find_parent(a),find_parent(b)
    if ar==br:
        continue
    elif ar>br:
        parent[ar]=br
    else:
        parent[br]=ar
    #print(cost)
    result+=cost
    last=cost
print(result-last)    
    