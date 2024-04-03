class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # https://leetcode.com/problems/word-search/discuss/4965052/96.45Easy-Solutionwith-explanation
        
        m = len(board)
        n = len(board[0])
        dir = [[0,1],[0,-1],[-1,0],[1,0]]
        
        # i,j for board
        # k for word
        def backtrack(i, j, k):
            # stop when we found the last character in word
            # meaning we already iterate from index 0 to k
            if k == len(word):
                return True
            
            # stop when index out of bound
            # or when the character in the board is not what we're looking for
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
                return False
            
            # when we reach here meaning that board[i][j] == word[k]
            # we'll start to search for adjacent cells
            # we mark the cell is visited by make it empty
            
            temp = board[i][j]
            board[i][j] = ''
            
            for x,y in dir:
                if backtrack(i+x,j+y,k+1):
                    return True
                
            # when we reach here meaning no recursive call found the word
            # we reset the cell and return False (to indicate this cell is not the character we're finding)
            board[i][j] = temp
            return False
        
        
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0): 
                    return True
        return False
            