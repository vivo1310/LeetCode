class Solution:
    def pivotInteger(self, n: int) -> int:
        i = 1
        while i < n + 1:
            if sum(range(1, i+1)) == sum(range(i, n + 1)):
                return i
            i += 1
        return -1