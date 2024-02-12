class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquaredDigits(n):
            res = 0
            while n >= 0:
                if n == 0:
                    break
                res += (n % 10) ** 2
                n = n // 10
            return res
        
        # Using Floyd's since it involves endless cycle
        slow = n 
        fast = sumSquaredDigits(slow)
        
        while slow != fast:
            slow = sumSquaredDigits(slow)
            fast = sumSquaredDigits(sumSquaredDigits(fast))
            
        if slow == 1: # happy number
            return True
        return False
        
        
        # Using hash set
#         hashSet = set()
        
#         while n != 1:
#             n = sumSquaredDigits(n)
#             if n in hashSet: # encounter cycle -> not happy number
#                 return False
#             else:
#                 hashSet.add(n)
#         return True