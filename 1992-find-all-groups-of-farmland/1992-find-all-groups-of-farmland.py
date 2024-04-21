class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        X, Y = len(land), len(land[0])
        
        def helper(x, y):
            stack = [(x,y)]
            visited.add((x,y))
            topLeftX, topLeftY = x,y
            bottomRightX, bottomRightY = x,y
            
            while stack:
                currX, currY = stack.pop()
                for dx, dy in directions:
                    newX, newY = currX + dx, currY + dy
                    
                    if 0 <= newX < X and 0 <= newY < Y \
                        and (newX, newY) not in visited \
                        and land[newX][newY] == 1:
                        stack.append((newX, newY))
                        visited.add((newX, newY))
                        topLeftX, topLeftY = min(newX, topLeftX), min(newY, topLeftY)
                        bottomRightX, bottomRightY = max(newX, bottomRightX), max(newY, bottomRightY)
            
            return [topLeftX, topLeftY, bottomRightX, bottomRightY]
        
        for i in range(X):
            for j in range(Y):
                if (i,j) not in visited and land[i][j] == 1:
                    farmland = helper(i,j)
                    result.append(farmland)
        return result
                        