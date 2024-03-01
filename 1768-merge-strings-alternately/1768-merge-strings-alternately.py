class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        i = 0
        res = ''
        while i < minLen:
            res += word1[i] + word2[i]
            i += 1
        if len(word1) > len(word2):
            res += word1[i:]
        elif len(word1) < len(word2):
            res += word2[i:]
        return res