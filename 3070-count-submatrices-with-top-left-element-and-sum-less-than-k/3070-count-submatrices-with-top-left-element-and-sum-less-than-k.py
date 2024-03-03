class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # create a prefix sum matrix
        # keep count of sum <= k
        R, C = len(grid), len(grid[0])
        
        ps = [[0] * (C + 1) for _ in range(R + 1)]
        
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                ps[i][j] = grid[i-1][j-1] + ps[i][j-1]
        # print(ps)
        count = 0
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                ps[i][j] += ps[i-1][j]
                if ps[i][j] <= k:
                    count += 1
        
        # count = 0
        # for i in range(1, R + 1):
        #     for j in range(1, C + 1):
        #         if ps[i][j] <= k:
        #             count += 1
                
        # print(ps)
        
        
        return count
        