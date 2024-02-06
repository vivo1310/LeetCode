class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use the first number of each row to identify which row we should search
        # eg. to find 3, we look at the first number of each row (1, 10 and 23)
        # it falls in the range of 1 to 10
        # so we search first row by using binary search
        # step 1: find the row by binary search the matrix
        # step 2: binary search the row
        
        # step 1 - O(logm) m is number of row
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                # target falls in the range of matrix[mid]
                break            
        
        # step 2 - O(logn) n is number of col
        nums = matrix[mid]
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
        # O(logm + logn) -> O(log(m*n))