s=input()
number=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
result=[]
def dfs(n1,string):
    if n1==len(data):
        result.append(string)
        return
    for i in range(len(data[n1])):
        dfs(n1+1,string+data[n1][i])
    
    
    

data=[]
for i in s:
    i=int(i)
    data.append(number[i])
dfs(0,'')
print(result)

    

    
    