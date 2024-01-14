class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(a,b):
            if len(a) < len(b):
                return False
            m = {}
            for c in a:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
            for c in b:
                if c not in m:
                    return False
                m[c] -= 1 # encounter the letter in the first phrase, decrease the frequency by -1
                if m[c] == 0:
                    m.pop(c) # if meet all occurances of that letter, remove that letter in the mapping
            return True if m == {} else False

        # two pointers, adjacent, do exactly what the problem describes
        # In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
        i = 1
        while i < len(words) :
            if isAnagram(words[i-1], words[i]):
                del words[i]
            else:
                i += 1
        return words
        