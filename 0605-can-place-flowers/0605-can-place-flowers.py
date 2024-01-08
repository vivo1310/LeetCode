class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 1 0 1 0 0 0 0 0 0 n = 3
        count = 0 # number of flowers that could be planted
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: # check if this is empty slot
                leftEmpty = (i == 0) or flowerbed[i-1] == 0
                rightEmpty = (i == len(flowerbed) - 1) or flowerbed[i+1] == 0
                if leftEmpty and rightEmpty:
#                     plant the flower in the empty slot
                    flowerbed[i] = 1
                    count += 1
        # if n < number of flowers that could be planted, return True
        return count >= n