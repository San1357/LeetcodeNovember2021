# Problem no.: 300
# Problem name : Longest Increasing Subsequence
# Topicc Dynammic Programming

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = len(nums)
        dp = [1] * length        # [1,1,1,1,1,1] in this case length = 8 
        #print("dp:",dp)
        for i in range(1,length):
            for j in range(i):
                #print("\ni:",i,"j:", j)
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        #print("\nOutput:",max(dp))
        return max(dp)
    
    
    #Space : O(n)
    #Time  : O(n**2)
    #Time complexity of max() = O(1)
