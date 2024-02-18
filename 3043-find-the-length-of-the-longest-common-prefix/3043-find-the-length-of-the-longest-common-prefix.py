class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # find all pairs
        # find longest common prefix, get length, set maxLength
        # return maxLength
        
        def getPrefixes(n):
            res = [n]
            while n > 9:
                n //= 10
                res.append(n)
            return res
        
        prefixes = set() # hashset of possible prefix of arr1
        for n in arr1:
            prefixes.add(n)
            while n > 9:
                n //= 10
                prefixes.add(n)
        print(prefixes)
            
        longest = 0
        for n in arr2:
            arr2Prefixes = getPrefixes(n)
            for p in arr2Prefixes:
                if p in prefixes:
                    currLength = len(str(p))
                    if currLength >= longest:
                        longest = currLength
            # if n in prefixes:
            #     currLength = len(str(n))
            #     if currLength >= longest:
            #         longest = currLength
            # while n > 9:
            #     n //= 10
        return longest