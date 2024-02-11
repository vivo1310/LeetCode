class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # n = 4
        # 00, 03
        # i forward
        # j will be n - 1 - i
        n = len(grid)
        for i in range(n):
            for j in range(n):
                cell = grid[i][j]
                if i == j or j == n-1-i:
                    if cell == 0:
                # (j == i and cell == 0 or 
                #     (j == n - 1 - i and cell == 0)):
                        print(i,j,cell)
                        return False
                elif cell != 0:
                    print(i,j,cell)
                    return False
        return True
            