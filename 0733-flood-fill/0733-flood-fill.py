class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R,C = len(image), len(image[0])
        sourcePixel = image[sr][sc]
        if sourcePixel == color:
            return image
    
        # define helper func dfs
        def dfs(r, c):
            if image[r][c] == sourcePixel: # need to update it to new color
                image[r][c] = color # updated
                # then paint the 4-directional adjacent cells
                if r >= 1:
                    dfs(r - 1, c) # up
                if r + 1 < R:
                    dfs(r + 1, c) # down
                if c >= 1:
                    dfs(r, c - 1) # left
                if c + 1 < C:
                    dfs(r, c + 1) # right
                    
        dfs(sr, sc)
        return image
        