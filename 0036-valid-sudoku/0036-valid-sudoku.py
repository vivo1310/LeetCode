class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDuplicate(nums): # nums is array
            hashMap = {}
            for n in nums:
                if n != ".":
                    if n not in hashMap:
                        hashMap[n] = 1
                    else:
                        return True
            return False

        # Check Rows
        # rows = []
        for i in range(9):
            row = board[i]
            if hasDuplicate(row):
                # print('a', row)
                return False
            
        # Check Cols
        cols = []
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            cols.append(col)
        for col in cols:
            if hasDuplicate(col):
                # print('b', cols)
                return False
        
        # Check Sub-boxes
        boxes = []
        for i in [0,3,6]:
            for j in [0,3,6]:
                box = []
                for k in range(3):
                    for l in range(3):
                        box.append(board[i+l][j+k])
                boxes.append(box)
        for box in boxes:
            if hasDuplicate(box):
                print('c', boxes)
                return False
        
        # print(cols)
        # print(boxes)
        return True
