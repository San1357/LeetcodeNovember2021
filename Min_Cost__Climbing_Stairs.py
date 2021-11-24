
# problem name : Min_Cost__Climbing_Stairs
# problem no. : 746


#Code :

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i):
            if i <=1:
                return 0
            if i not in memo:
                
                one = cost[i-1] + dp(i-1)
                two = cost[i-2] + dp(i-2)
                
                memo[i] = min(one,two)
            return memo[i]
        
        memo = {}
        return dp(len(cost))
      

#time : O(N)
#Space : O(N)
                










