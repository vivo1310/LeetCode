class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # def getLetterFrequencyMap(word):
        #     freqMap = {}
        #     i = 0
        #     while i < len(word):
        #         letter = word[i]
        #         if letter in freqMap:
        #             freqMap[letter] += 1
        #         else:
        #             freqMap[letter] = 1
        #         i += 1
        #     return freqMap
        # if len(s) != len(t):
        #     return False
        # return getLetterFrequencyMap(s) == getLetterFrequencyMap(t)


        if len(t) < len(s):
            return False
        smap = {}
        for c in s:
            smap[c] = 1 + smap.get(c, 0) # short version for the below
            # if c in smap:
            #     smap[c] += 1
            # else:
            #     smap[c] = 1
        for c in t:
            if c not in smap:
                return False
            smap[c] -= 1
            if smap[c] == 0:
                smap.pop(c)
        return True if smap == {} else False
        