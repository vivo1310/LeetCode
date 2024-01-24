class Solution:
    def tribonacci(self, n: int) -> int:
#         DP - Tabulation
        t = {}
        t[0] = 0
        t[1] = 1
        t[2] = 1
        if n in t:
            return t[n]
        
        for i in range(3, n + 1):
            t[i] = t[i-1] + t[i-2] + t[i-3]
            
        return t[n]