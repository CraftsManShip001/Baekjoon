n = int(input())
dp = [1,1,0,1,1]
for i in range(5,n+1):   
        if dp[i-1] + dp[i-3] + dp[i-4] == 3 :
            dp.append(0)
        else :
            dp.append(1)
if dp[n] == 1 :
    print("SK")
else :
    print("CY")