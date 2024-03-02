class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square then sort
        sq = []
        for n in nums:
            sq.append(n**2)
        print(sq.sort())
        return sq