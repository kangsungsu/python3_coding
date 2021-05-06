import copy
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    i=0
    n=len(food_times)
    food=[]
    for i in range(len(food_times)):
        food.append([food_times[i],i+1])
    food.sort()
    zero=0
    while k>=n*food[zero][0]:
        m=food[zero][0]
        for i in food[zero:]:
            i[0]-=m
        for x in range(zero,len(food)):
            if food[x][0]!=0:
                break
        k-=n*m
        n-=x
        zero=x
        print(food)
    f=[0]*(len(food_times)+1)
    
    for i in range(len(food_times)):
        
        if food[i][0]!=0:
            break
        f[food[i][1]]+=1
    print(f,k)
solution([3,1,2],4)