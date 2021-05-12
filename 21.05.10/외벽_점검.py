from collections import deque
import copy
def solution(n, weak, dist):
    answer = 0
    space=[]
    if len(weak)==1:
        return 1
    for i in range(len(weak)):
        if i==len(weak)-1:
            space.append((n-weak[i]+weak[0],weak[i]))
            continue
        space.append((weak[i+1]-weak[i],weak[i]))
    space.sort(reverse=True)
    dist.sort(reverse=True)
    for i in range(len(dist)):
        nSpace=copy.deepcopy(space)
        for j in range(i):
            n,x= b



    return answer

solution(12,[1, 5, 6, 10],[1, 2, 3, 4])