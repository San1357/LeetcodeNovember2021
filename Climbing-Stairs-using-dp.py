

# Problem name : Climbing stairs
# Problem no. : 70 


#Code :


class Solution:
    def climbStairs(self, n: int) -> int:
       if i == 1:
          return 1
       dp = [0]*(n+1)
       dp[1] = 1
       dp[2] = 2
       for i  in range(3,n+1):
          dp[i] = dp[i-1] + dp[i-2]
       
       return dp[n]
            
        
        # bottom up approach
        
        
        # time : O(N)
        # space : O(N)

