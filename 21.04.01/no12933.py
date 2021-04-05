import copy

sound=list(input())
result=0
fail_check=[0]*5
for i in range(len(sound)):
    
    if sound[i]=='q':
        fail_check[0]+=1
    elif sound[i]=='u':
        fail_check[1]+=1
    elif sound[i]=='a':
        fail_check[2]+=1
    elif sound[i]=='c':
        fail_check[3]+=1
    else:
        fail_check[4]+=1
    x=copy.deepcopy(fail_check)
    #print(fail_check)
    x.sort(reverse=True)
    #print(x)
    if(x!=fail_check):
        print(-1)
        exit(0)
    if sound[i]!='q':
        continue
    data=[0]*5
    for j in range(i,len(sound)):
        #print(data)
        
        
        if sound[j]=='q':
            data[0]+=1
        elif sound[j]=='u':
            data[1]+=1
        elif sound[j]=='a':
            data[2]+=1
        elif sound[j]=='c':
            data[3]+=1
        else:
            data[4]+=1
        if 0 not in data:

            result=max(max(data),result)
            break
print(result)

            