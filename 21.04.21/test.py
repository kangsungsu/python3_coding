height = [1,8,6,2,5,4,8,3,7]
maxarea,front,back=0,0,len(height)-1
while front<back:
    maxarea=max(maxarea,min(height[front],height[back])*(back-front))
    if height[front]<height[back]:
        front+=1
    else:
        back-=1
print(maxarea)