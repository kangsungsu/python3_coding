s=input()
sum=0
st=[]
for i in s:
    if i.isdigit():
        sum+=int(i)
    else:
        st.append(i)

print(*sorted(st),sum,sep='')