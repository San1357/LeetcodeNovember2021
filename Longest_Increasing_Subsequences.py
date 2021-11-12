# Problem no. : 300
# Problem name: Longest Integer Subbsequence

#CODE:

class Solution:
  def LengthofLIS(self, nums: List[int])-> int:
    
    sub = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] > sub[-1]:
            sub.append(nums[i])
        else:
            j = 0
            while nums[i] > sub[j]:
                j+=1
            sub[j] = nums[i]
    
    return len(sub)

#time : O(N^2)
#Space : O(N)
        
        
