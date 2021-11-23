#time : O(NlogN)
#space : O(N)
# Problem name : Russian-Doll-Envelopes
# Problem  no.: 354

#CoDe: 

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print("envelopes:",envelopes)
        increasing = [envelopes[0][1]]
        print(increasing)

        for i in range(1, len(envelopes)):
            if increasing[-1] < envelopes[i][1]:
                increasing.append(envelopes[i][1])
            else:
                left = 0
                right = len(increasing)-1
                while left < right:
                    mid = (left+right)//2

                    if increasing[mid] < envelopes[i][1]:
                        left = mid+1
                    else:
                        right = mid

                increasing[left] = envelopes[i][1]

        return len(increasing)
