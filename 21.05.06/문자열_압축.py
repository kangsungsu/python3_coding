def solution(s):
    answer = 0
    l=len(s)
    mini=[]
    for i in range(1,l+1):
        j=0
        m=0
        a=[]
        while j+2*i<=l:
            #print('a',a,'m',m,'j',j,'i',i)
            if s[j:j+i]==s[j+i:j+2*i]:
                m+=1
                j+=i
                
            else:
                if m!=0:
                    a.append(m+1)
                    m=0
                j+=i
                continue
        if m!=0:
            a.append(m+1)
        
        r=0
        print(a)
        for j in a:
            
            r+=len(str(j))
        r+=len(a)*i           
        mini.append(r+l-sum(a)*i)
        print(a,r,l,i,r+l-sum(a)*i)
    return min(mini)