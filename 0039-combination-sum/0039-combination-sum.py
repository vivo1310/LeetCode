class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start = 0, total = 0, comb = []):
            if target == total:
                res.append(comb.copy())
                return
            else:
                for i in range(start, len(candidates)):
                    if total + candidates[i] <= target:
                        backtrack(i, total + candidates[i], comb + [candidates[i]])
                
            
        backtrack()
        return res
    