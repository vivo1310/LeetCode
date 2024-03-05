class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                while i + 1 < len(s) and s[i +1 ] == s[i]:
                    i += 1
                while j - 1 > 0 and s[j-1] == s[j]:
                    j -= 1
                s = s[i + 1:j]
                i, j = 0, len(s) - 1
            else:
                return len(s)
        return len(s)