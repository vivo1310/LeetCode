class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wordMapS = {}
        wordMapT = {}
        
        for i in range(len(s)):
            if s[i] not in wordMapS:
                wordMapS[s[i]] = t[i]
            elif wordMapS[s[i]] != t[i]:
                return False
            if t[i] not in wordMapT:
                wordMapT[t[i]] = s[i]
            elif wordMapT[t[i]] != s[i]:
                return False
        return True
                