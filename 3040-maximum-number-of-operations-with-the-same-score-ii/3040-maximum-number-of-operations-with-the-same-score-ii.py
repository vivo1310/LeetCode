class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache # to not use extra dp map to manually cache
        def solve(i = 0, j = n-1 , score = 0):
            if i >= j:
                return 0
            
            a = b = c = 0
            if score == 0 or nums[i] + nums[i+1] == score:
                a = 1 + solve(i + 2, j, nums[i] + nums[i+1])
            if score == 0 or nums[j] + nums[j-1] == score:
                b = 1 + solve(i, j - 2, nums[j] + nums[j-1])
            if score == 0 or nums[i] + nums[j] == score:
                c = 1 + solve(i + 1, j - 1, nums[i] + nums[j])
            return max(a,b,c)
        
        return solve()
    
#         def solve(i, j, score):
#             # i at the first, j at the last position
#             if i >= j:
#                 return 0
#             if (i,j) in dp:
#                 return dp[(i,j)]

#             ans = 0
#             if nums[i] + nums[i+1] == score: 
#                 # Choose the first two elements of nums
#                 ans = max(ans, 1 + solve(i + 2, j, nums[i] + nums[i+1]))
#             if nums[j] + nums[j-1] == score:
#                 # Choose the last two elements of nums
#                 ans = max(ans, 1 + solve(i, j - 2, nums[j] + nums[j-1]))
#             if nums[i] + nums[j] == score:
#                 # Choose the first and the last elements of nums
#                 ans = max(ans, 1 + solve(i + 1, j - 1, nums[i] + nums[j]))

#             dp[(i,j)] = ans
#             return ans
                          
#         dp = {}
#         i, j = 0, len(nums) - 1
#         res = 1 + max(solve(i + 2, j, nums[i] + nums[i+1]),
#                   solve(i, j - 2, nums[j] + nums[j-1]),
#                   solve(i + 1, j - 1, nums[i] + nums[j]))

#         return res
        