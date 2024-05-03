class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        print(word.find(ch))
        i = word.find(ch) # index of first occurance of ch
        
        if i > 0:
            pref = word[:i+1]
            remaining = word[i+1:]
            return pref[::-1] + remaining
            
        return word
        