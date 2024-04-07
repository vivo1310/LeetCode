class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # make 2 pass, 1 from LTR, the other from RTL
        # LTR: if encounter closing but stack is empty, remove
        # RTL:              open bracket 
        def makePass(c1, c2, s):
            stack = []
            i = 0
            res = [] # res when finish first pass (LTR)

            while i < len(s):
                if s[i] == c2:
                    if not stack:
                        i += 1
                        continue
                    else:
                        stack.pop()
                elif s[i] == c1:
                    stack.append(s[i])
                res.append(s[i])
                i+=1
            return "".join(res)
        
        temp = makePass("(",")",s)
        return makePass(")","(",temp[::-1])[::-1]