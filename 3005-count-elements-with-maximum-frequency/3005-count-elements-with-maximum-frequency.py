class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        # maxFreq = max(counter.values())
        count = 0
        maxFreq = 0
        for v in counter.values():
            if v > maxFreq:
                maxFreq = v
                count = v
                # print('a', maxFreq, count)
            elif v == maxFreq:
                count += v
                # print('b', maxFreq, count)
                
        # print(counter, maxFreq)
        return count