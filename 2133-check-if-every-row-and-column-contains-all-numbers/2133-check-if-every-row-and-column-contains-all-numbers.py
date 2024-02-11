class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] in rows[i] or matrix[i][j] in cols[j]:
                    # print(i,j,matrix[i][j])
                    return False
                else:
                    rows[i].add(matrix[i][j])
                    cols[j].add(matrix[i][j])
        # print(rows, cols)
        return True
                