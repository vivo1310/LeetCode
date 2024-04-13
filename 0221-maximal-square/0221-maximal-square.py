class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        cache = {} # map each (r,c) -> maxArea
        
        def helper(r, c):
            # check for out of bound, return 0 as no more cell to form square
            if r >= R or c >= C:
                return 0
            
            # calculate max area at the cell
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diagonal = helper(r + 1, c + 1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diagonal)
                
            return cache[(r,c)]
        
        helper(0, 0)
        
        return max(cache.values()) ** 2
                    
            