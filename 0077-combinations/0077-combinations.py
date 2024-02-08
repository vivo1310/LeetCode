class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(comb = [], start = 1):
            if k == len(comb):
                res.append(comb.copy())
                return
            else:
                for i in range(start, n + 1):
                    backtrack(comb + [i], i + 1)
            
        backtrack()
        return res