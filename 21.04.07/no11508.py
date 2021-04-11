n=int(input())
data=[]
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)
s=0
for i in range(2,n,3):
    s+=data[i]
print(sum(data)-s)