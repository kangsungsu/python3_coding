n,m,k=map(int,input().split())

data=list(map(int,input().split()))
data.sort(reverse=True)
first=data[0]
second=data[1]
num=(k-1)*first+second
print(num*(m//k)+n%k*first)