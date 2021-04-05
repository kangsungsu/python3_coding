arr=[]
n=int(input())
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
sum=0
for i in range(len(arr)):
    if arr[i]-i>0:
        sum+=arr[i]-i
print(sum)