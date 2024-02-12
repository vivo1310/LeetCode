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
        
        hashSet = set()
        
        while n != 1:
            n = sumSquaredDigits(n)
            if n in hashSet:
                return False
            else:
                hashSet.add(n)
        return True