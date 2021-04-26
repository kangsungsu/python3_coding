num=int(input())
t,p,dp=[],[],[]
for _ in range(num):
    tn,pn=map(int,input().split())
    t.append(tn)
    p.append(pn)
    dp.append(pn)
dp.append(0)

    

for i in range(num - 1, -1, -1):
    if t[i] + i > num:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])



    