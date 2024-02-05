class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use the first number of each row to identify which row we should search
        # eg. to find 3, we look at the first number of each row (1, 10 and 23)
        # it falls in the range of 1 to 10
        # so we search first row by using binary search
        # step 1: find the row
        # step 2: binary search the row
        # step 1
        R = 0
        for i in range(len(matrix)):
            row = matrix[i]
            if target >= row[0]:
                R = i
                
        # step 2
        nums = matrix[R]
        l,r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2 
            if target == nums[m]:
                return True
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return False