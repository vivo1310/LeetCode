class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # start from the square root and find the pair of L,W 
        # to make sure requirement #3 is satisfied
        
        x = int(sqrt(area))
        
        while True:
            if area % x == 0: # found L,W pair
                return [area // x, x] # [L, W] where L >= W
            x -= 1