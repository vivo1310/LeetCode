class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        hashMap = {}
        for n in nums:
            # cal sum of digit of n
            temp = n
            digitSum = 0
            while temp:
                digitSum += temp % 10
                temp = temp // 10
            
            # add to hashMap key is digit sum and value is max of n and prev max
            if digitSum not in hashMap:
                hashMap[digitSum] = n
            else:
                # set res only when we have a equal digit sum pair
                res = max(hashMap[digitSum] + n , res)
                hashMap[digitSum] = max(n, hashMap[digitSum])
        return res
            
        
        
                