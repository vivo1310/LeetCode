class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # {count, index}
        hm = {0:-1}
        
        # when see 0, decrement count by 1
        # when see 1, increment count by 1
        # when count between 2 index same -> the subarray is having equal 0s and 1s
        # [0,0,1,1,0,1]
        # -1-2-1 0 -1 0
        count = 0
        best = 0
        
        for i, n in enumerate(nums):
            if n == 0:
                count += -1
            else:
                count += 1
            if count in hm:
                best = max(best, i-hm[count])
            else:
                hm[count] = i
            # print(hm, count, best)
        return best