class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # count = 0 # number of flowers that could be planted
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: # check if this is empty slot
                leftEmpty = (i == 0) or flowerbed[i-1] == 0
                rightEmpty = (i == len(flowerbed) - 1) or flowerbed[i+1] == 0
                if leftEmpty and rightEmpty:
#                     plant the flower in the empty slot
                    flowerbed[i] = 1
                    n -= 1
                    # count += 1
        # if n < number of flowers that could be planted, return True
        # return count >= n
        return n <= 0
    
    
    
#     Instead of using that super long 'if condition'. Its better to add 0 at the start and end of the list. Makes it cleaner and easier to understand!
#         bed = [0] + flowerbed + [0]
#         for i in range(1, len(flowerbed) + 1):
#             if bed[i] == bed[i-1] == bed[i+1] == 0:
# #                 plant it
#                 bed[i] = 1
#                 n -= 1
#             if n <= 0: return True
#         return False