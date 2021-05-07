n=list(map(int,input()))
#print(n[:len(n)//2],(n[len(n)//2:]))
if sum(n[:len(n)//2])==sum(n[len(n)//2:]):
    print('LUCKY')
else:
    print('READY')