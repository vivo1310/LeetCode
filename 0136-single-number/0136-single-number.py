class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        # print(freq)
        for k,v in freq.items():
            if v == 1:
                return k