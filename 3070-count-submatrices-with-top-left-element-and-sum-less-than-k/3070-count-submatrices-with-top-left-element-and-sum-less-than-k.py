class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # O(R*C) for time and O(1) for space
        # create a prefix sum matrix 
        # keep count of sum <= k
#         R, C = len(grid), len(grid[0])
            
#         for i in range(R):
#             for j in range(1, C):
#                 grid[i][j] += grid[i][j-1]

#         for j in range(C):
#             for i in range(1, R):
#                 grid[i][j] += grid[i-1][j]
                
#         count = 0
#         for i in range(R):
#             for j in range(C):
#                 if grid[i][j] <= k:
#                     count += 1
#         return count

        # better version
        R, C = len(grid), len(grid[0])
        c = 0
        s = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                q = grid[i][j]
                if i > 0:
                    q += s[i-1][j]
                if j > 0:
                    q += s[i][j-1]
                if i > 0 and j > 0:
                    q -= s[i-1][j-1]
                s[i][j] = q
                if q <= k:
                    c += 1
        # print(s)
        return c
      