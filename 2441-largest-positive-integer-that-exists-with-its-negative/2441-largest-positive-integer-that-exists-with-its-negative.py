class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hm = {}
        arr = [] # satisfying k
        for n in nums:
            if -n in hm:
                arr.append(abs(n))
            else:
                hm[n] = 0
        # print(arr)
        return max(arr) if arr else -1
                
                