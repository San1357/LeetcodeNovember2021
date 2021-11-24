#Problem name: N-th Tribonacci Number
#Problem no.: 1137
#time : O(N)
#space : 
#top-down approach

#Code : 

class Solution:
    def tribonacci(self, n: int) -> int:
        def  dp(i):
            if i==0:
                return 0
            if i<=2:
                return 1
            if i not in memo:
                memo[i] = dp(i-1)+dp(i-2)+dp(i-3)
            return memo[i]
        
        memo = {}
        return dp(n)
