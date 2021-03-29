from collections import deque
n,m=map(int,input().split())
order=[[] for i in range(n)]
student=[0 for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    student[b-1]+=1
    order[a-1].append(b-1)

que=deque()
for i in range(len(student)):
    if student[i]==0:
        que.append(i)

answer=[]
while que:
    i=que.popleft()
    answer.append(i+1)
    for i in order[i]:
        student[i]-=1
        if student[i]==0:
            que.append(i)

print(answer)



