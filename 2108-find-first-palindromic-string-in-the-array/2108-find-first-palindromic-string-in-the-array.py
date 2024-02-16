class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            i, j = 0, len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        return ""
            
        