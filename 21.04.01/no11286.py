import heapq
num=int(input())
data=[]
ord=[]
heapq.heapify(data)
for i in range(num):
    ord.append(int(input()))
for i in ord:
    
    if i!=0:
        heapq.heappush(data,(abs(i),i))
    else:
        if len(data)==0:
            print(0)
        else:
            print(heapq.heappop(data)[1])
