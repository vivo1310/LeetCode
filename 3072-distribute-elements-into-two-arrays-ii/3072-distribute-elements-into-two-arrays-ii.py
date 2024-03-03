from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        s1 = SortedList(arr1)
        s2 = SortedList(arr2)

        # doing greaterCount by sort arr
        for x in nums[2:]:
            a = len(arr1) - s1.bisect_right(x)
            b = len(arr2) - s2.bisect_right(x)

            if a > b:
                q = 1 # add to arr1
            elif a < b:
                q = 2 # add to arr2
            else:
                if len(arr1) > len(arr2):
                    q = 2
                else:
                    q = 1
                    
            if q == 1:
                arr1.append(x)
                s1.add(x)
            else:
                arr2.append(x)
                s2.add(x)
        return arr1 + arr2