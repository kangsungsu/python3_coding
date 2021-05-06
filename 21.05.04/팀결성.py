n,m=map(int,input().split())

parent=[i for i in range(n+1)]
print(parent)

def find_parent(x):
    if parent[x]!=x:
        return find_parent(parent[x])
    return x

for i in range(m):
    a,b,c=map(int,input().split())
    br,cr=find_parent(b),find_parent(c)
    if a==0:
        
        if br>cr:
            parent[br]=cr
        else:
            parent[cr]=br
    else:
        if br==cr:
            print("YES")
        else:
            print("NO")
        


