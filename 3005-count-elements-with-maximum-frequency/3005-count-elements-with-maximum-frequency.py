class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        count = 0
        maxFreq = 0
        for v in counter.values():
            if v > maxFreq:
                maxFreq = v
                count = v
            elif v == maxFreq:
                count += v
                
        return count