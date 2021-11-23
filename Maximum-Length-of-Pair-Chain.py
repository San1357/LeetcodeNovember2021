# UsinG LIS
# Time complexity  : O(N^2)
# Space complexity : O(N)
# Problem name : Maximum-Length-of-Pair-Chain
# Problem no. : 646



#CODE :

class Solution(object): #Time Limit Exceeded
    def findLongestChain(self, pairs):
       pair = sorted(pairs)
       
       dp = [1]*len(pair)
        
       for i in range(1, len(pair)):
            for j in range(i):
                if pair[i][1] < pair[j][0]:
                    dp[i] = max(dp[i]+dp[j]+1)
       return max(dp)
          
