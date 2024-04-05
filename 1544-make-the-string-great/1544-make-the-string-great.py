class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while 0 <= i <= len(s) - 2:
            if abs(ord(s[i]) - ord(s[i+1])) == 32: # s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i += 1
        return s