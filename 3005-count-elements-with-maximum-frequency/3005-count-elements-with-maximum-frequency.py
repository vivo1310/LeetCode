class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # O(2n) Time O(n) Space
#         counter = collections.Counter(nums)
#         count = 0
#         maxFreq = 0
#         for v in counter.values():
#             if v > maxFreq:
#                 maxFreq = v
#                 count = v
#             elif v == maxFreq:
#                 count += v
                
#         return count
    
        # Above is O(2n), combine the 2 loops to O(N)
        hm = {}
        maxFreq = 0
        count = 0
        for n in nums:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] += 1
            v = hm[n]
            if v > maxFreq:
                maxFreq = v
                count = v
            elif v == maxFreq:
                count += v
        return count