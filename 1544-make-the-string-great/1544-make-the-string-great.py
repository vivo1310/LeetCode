class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while 0 <= i <= len(s) - 2:
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                # print('bef', s, i)
                s = s[:i] + s[i+2:]
                i = 0
                # print('aft',s,i)
            else:
                i += 1
        return s