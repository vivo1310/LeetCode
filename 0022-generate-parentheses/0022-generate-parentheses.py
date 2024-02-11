class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open, close = 0, 0
        res = []
        
        def backtrack(comb = "", open = 0, close = 0):
            if open == n and close == n:
                res.append(comb)
                return
            
            if open < n:
                comb += "("
                backtrack(comb, open + 1, close)
                comb = comb[:-1]

            if open > close:
                comb += ")"
                backtrack(comb, open, close + 1)
                comb = comb[:-1]

        backtrack()
        return res