mo=['a','e','i','o','u']


while True:
    s=input()
    if s=='end':
        break
    check1=0
    for i in mo:
        if i in s:
            check1+=1
            break
    
    if check1==0:
        print('<'+s+'> is not acceptable.')
        continue
    check2=''
    for i in s:
        if i in mo:
            check2+='m'
        else:
            check2+='j'
    #print(check2)
    if ('mmm' in check2) or ('jjj' in check2):
        print('<'+s+'> is not acceptable.')
        continue
    check3=0
    for i in range(len(s)-2):
        if s[i]==s[i+1] and s[i]!='e' and s[i]!='o':
            print('<'+s+'> is not acceptable.')
            check3=1
            break
    if check3==0:
        print('<'+s+'> is acceptable.')
        

            


    
         