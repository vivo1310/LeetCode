class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        # 2 pointer, 1 go forward, 1 go backward
        # primary is sum of mat[i][i]
        # secondary is sum of mat[i][j]
        
        i, j = 0, n-1
        while i < n:
            total += mat[i][i]
            total += mat[i][j]
            if n % 2 != 0 and i == j:
                total -= mat[i][j]
            i += 1
            j -= 1
        return total