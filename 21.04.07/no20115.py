num=int(input())

data=list(map(int,input().split()))
data.sort(reverse=True)
print(data[0]+sum(data[1:])/2)
    
