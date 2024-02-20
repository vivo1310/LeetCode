class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # constraint 10^4 => aim for O(nlogn)
#         nums.sort() # O(nlogn)
        
#         for i in range(nums[-1]):
#             if i != nums[i]:
#                 return i
#         return nums[-1] + 1
    
        # Follow up: ask for O(1) space and O(n)?
        # Sum all numbers S O(n) T O(n)
        # 0 1 2 3 4 -> n=4 -> sum=1+2+3+4=10
        # n = len(nums)
        # expectedSum = sum([x for x in range(n+1)])
        # actualSum = 0
        # for n in nums:
        #     actualSum += n
        # return expectedSum - actualSum
    
        # Hashmap S O(n) T O(n)
        n = len(nums)
        arr = [-1 for x in range(n+1)]
        for num in nums:
            arr[num] = num
            
        for i, num in enumerate(arr):
            if num == -1: return i
        
        
        
        