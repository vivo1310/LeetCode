class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make two passes, first in-order, second in-reverse, to compute products
        # [1,2,6,24]
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prod = nums[i]
            else:
                prod = nums[i] * prefix[i-1]
            prefix.append(prod)
        # print(prefix)
        
        # [24,24,12,4]
        postfix = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                prod = nums[i]
            else:
                prod = nums[i] * postfix[i+1]
            postfix[i] = prod
        # print(postfix)
        
        res = []
        
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        return res
     