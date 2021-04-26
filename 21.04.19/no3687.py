num=int(input())
def small(n):
    str=''
    if n%7==0:
        
        for i in range(n//7):
            str+='8'
    elif n==2:
        return 1
    elif n==3:
        return 7
    elif n==4:
        return 4
    elif n==5:
        return 2
    elif n==6:
        return 6
    elif n==7:
        return 8
    elif n==11:
        return 20
    elif n==10:
        return 22
     
    else:
        m=n//7-1
        k=n-m*7
        if k==8:
            str+='10'
        elif k==9:
            str+='18'
        elif k==10:
            str+='20'
        elif k==11:
            str+='20'
        elif k==12:
            str+='28'
        elif k==13:
            str+='68'
        for i in range(m):
            if i==0 and k==10:
                str+='0'
            str+='8'
        if k==10:
            return str[:-1]
    return str

def big(n):
    str=''
    if n%2==0:
        for i in range(n//2):
            str+='1'
    else:
        m=n//2-1
        str+='7'
        for i in range(m):
            str+='1'
    return str

            
        

            

for _ in range(num):
    n=int(input())
    print(small(n),big(n))
     

        
