import math
def solution(n):
    
    data=[0,3,11]
    for i in range(3,n//2+1):
        sum=0
        sum+=3*data[i-1]+2
        for j in range(1,i-1):
            sum+=2*data[j]
            #print(i,sum)
        data.append(sum)
    return (data[n//2]%1000000007)
        


        
        
        
print(solution(8))