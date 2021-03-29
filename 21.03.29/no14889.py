from itertools import combinations

n=int(input())
data=[]
result_array=[]
for i in range(n):
    data.append(list(map(int,input().split())))
for i in combinations([x for x in range(n)],n//2):
    var=0
    for j in combinations(i,2):
        var+=(data[j[0]][j[1]]+data[j[1]][j[0]])
        
    result_array.append(var)
val=1000000000
length=len(result_array)
for i in range(length//2):
    val=min(val,abs(result_array[i]-result_array[length-1-i]))
print(val)
    

