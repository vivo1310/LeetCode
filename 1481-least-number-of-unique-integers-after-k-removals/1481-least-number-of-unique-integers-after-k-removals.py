class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # create mapping: num -> freq
        # create mapping: freq -> [nums]
        # decrement k starting from the least frequent 
        # O(n*m) where n is len(arr) and m is max frequency
        count = Counter(arr) # O(n)
        res = len(count)
        
        freqMap = defaultdict(list)
        for key, val in count.items(): # O(n)
            freqMap[val].append(key)
    
        # a number can occur at most n time, eg. arr = [1,1,1]
        i = 1
        temp = i
        while i < len(count) + 1: # O(n)
            while k > 0 and temp > 0 and freqMap[i]:
                k -= 1
                temp -= 1
                if temp == 0:
                    freqMap[i].pop()
                    res -= 1
                    temp = i
            i += 1
            temp = i
                  
        
        return res