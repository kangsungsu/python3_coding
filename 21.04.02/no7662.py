import heapq
num=int(input())
for i in range(num):
    h=[]
    num2=int(input())
    for j in range(num2):
        s,n=input().split()
        n=int(n)
        if s=='I':
            heapq.heappush(h,n)
        elif s=='D' and len(h)==0:
            continue
        elif s=='D' and n==-1:
            heapq.heappop(h)

        else:
            h.pop()
    if len(h)==0:
        print('EMPTY')
    elif len(h)==1:
        print(h[0])
    else:
        print(h[len(h)-1],h[0])