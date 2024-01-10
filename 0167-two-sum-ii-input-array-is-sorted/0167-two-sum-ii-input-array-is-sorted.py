class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use 2 pointers, at the start and the end of the list
        # since the list is sorted, check
        # if sum > target, move j to the left, j--
        # if sum < target, move i forward, i++
        # if sum == target, return index
        # since guarantee 1 solution, iterate til i > j or iterate half number of item in the list
        i = 0
        j = len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i+1, j+1]
            elif s > target:
                j -= 1
            elif s < target:
                i += 1
        
                
        