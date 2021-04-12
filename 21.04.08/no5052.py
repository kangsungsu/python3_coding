
num1=int(input())
for i in range(num1):
    data=[]
    result="YES"
    num2=int(input())
    for j in range(num2):
        data.append(input())
    data.sort()
    for j in range(num2-1):
        #print(data[j],data[j+1][:len(data[j])])
        if data[j]==data[j+1][:len(data[j])]:
            result="NO"
            break
    print(result)

