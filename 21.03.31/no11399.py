num=int(input())

data=list(map(int,input().split()))
data.sort()
sum=0
for i in range(num):
    sum+=data[i]*(num-i)
print(sum)