class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            n = len(str1)
            if str1 == str2[:n] and str1 == str2[-n:]:
                return True
            return False
        
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)): # O(n^2) due to contraints is ~50 only
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count