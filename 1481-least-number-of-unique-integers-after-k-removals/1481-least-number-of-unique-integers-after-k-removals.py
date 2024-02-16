class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # create mapping: num -> freq
        # create mapping: freq -> [nums]
        # decrement k starting from the least frequent
        count = Counter(arr) # O(n)
        print(count)
        res = len(count)
        
        freqMap = defaultdict(list)
        for key, val in count.items():
            freqMap[val].append(key)
    
        print(freqMap)

        # for i in range(1, len(count) + 1): # a number can occur at most n time, eg. arr = [1,1,1]
        i = 1
        temp = i
        while i < len(count) + 1:
            # if not freqMap[i]:
            #     i += 1
            #     temp = i
            # temp = i
            while k > 0 and temp > 0 and freqMap[i]:
                k -= 1
                temp -= 1
                if temp == 0:
                    freqMap[i].pop()
                    res -= 1
                    temp = i
            i += 1
            temp = i
            # if not freqMap[i]:
            #     i += 1
            # else:
            #     while k > 0 and temp > 0:
            #         k -= 1
            #         temp -= 1
            #         if temp == 0:
            #             freqMap[i].pop()
            #             res -= 1
#             temp = i
#             while k > 0 and temp > 0 and freqMap[i]:
#                 k -= 1 # decrement k
#                 temp -= 1
#                 if temp == 0:
#                     removed = freqMap[i].pop() # and remove the number
#                     print(freqMap, removed, k)
#                     res -= 1
#                     # if not freqMap[i]:
#                     #     freqMap[i-1].append(removed)

#             i += 1
        print(freqMap)
        
        
        return res