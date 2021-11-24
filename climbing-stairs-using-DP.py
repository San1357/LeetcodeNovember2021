
# Problem no: 70
# Problem name:  Climbing  stairs

#CODE :

class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            
            if i < 3:
                return i
            if i  not in memoization_variable:
                memoization_variable[i] = dp(i-1) + dp(i-2)
            
            return  memoization_variable[i]
       
        memoization_variable = {}
        return dp(n)
            
        
        # Top-down (recursion + memoization)
        
        
        # time : O(N)
        # space : O(N)
        
        
    
