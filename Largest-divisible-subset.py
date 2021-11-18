# problem no : 368
# Problem name : Largest divisible Subset

#time complexity : O(n2)
#space : O(n)
#COde :


class Solution:
    def largestDivisibleSubset(self,nums):
        sorted_nums = sorted(nums)
        
        dp = [1] * len(sorted_nums)
        
        for i in range(1, len(sorted_nums)):
            for j in range(i):
                if sorted_nums[i] % sorted_nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] +1)
                    
        max_Index = 0
        for i in range(1, len(sorted_nums)):
            if dp[i] > dp[max_Index]:
                max_Index = i
        
        result = []
        temp = sorted_nums[max_Index]
        current_dp = dp[max_Index]
        for i in range(max_Index,-1,-1):
            if temp % sorted_nums[i] and current_dp[i] == dp[i]:
                result.append(sorted_nums[i])
                temp = sorted_nums[i]
                current_dp -= 1
                
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
