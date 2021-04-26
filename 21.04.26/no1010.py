import math
num=int(input())
for i in range(num):
    n,m=map(int,input().split())
    print(math.factorial(m)//(math.factorial(n)*math.factorial(m-n)))