from sortedcontainers import SortedList
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        s1 = SortedList(arr1)
        s2 = SortedList(arr2)

        # doing greaterCount by sort arr
        for i in range(2,len(nums)):
            a = len(arr1) - s1.bisect_right(nums[i])
            b = len(arr2) - s2.bisect_right(nums[i])

            if a > b:
                arr1.append(nums[i])
                s1.add(nums[i])
            elif a < b:
                arr2.append(nums[i])
                s2.add(nums[i])
            else:
                if len(arr1) < len(arr2):
                    arr1.append(nums[i])
                    s1.add(nums[i])
                elif len(arr1) > len(arr2):
                    arr2.append(nums[i])
                    s2.add(nums[i])
                else:
                    arr1.append(nums[i])
                    s1.add(nums[i])
        return arr1 + arr2