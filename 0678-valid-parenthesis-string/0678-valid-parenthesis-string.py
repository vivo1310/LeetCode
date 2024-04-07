class Solution:
    def checkValidString(self, s: str) -> bool:
        # count number of (, ) and *

        o = 0
        c = 0
        
        for i in range(len(s)):            
            if s[i] == "(" or s[i] == "*":
                o += 1
            else:
                o -= 1
            
            j = len(s) - 1 - i # iterate backwards
            if s[j] == ")" or s[j] == "*":
                c += 1
            else:
                c -= 1
            
            # at any point if open count or close count become negative, the string is invalid
            if c < 0 or o < 0:
                return False
        
        return True
            
      