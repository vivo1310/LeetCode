class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # lst = list(s)
        counter = Counter(s)
        res = ''
        for i in range(counter['1'] - 1):
            res += '1'
        for i in range(counter['0']):
            res += '0'
        res += '1' # s contains at least one '1'
        return res
        