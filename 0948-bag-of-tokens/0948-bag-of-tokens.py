from sortedcontainers import SortedList

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        sortedTokens = SortedList(tokens)
        
        # print(sortedTokens, sortedTokens[0], sortedTokens[-1])
        
        # when power >= min token, face-up, pop(0), score += 1, decrease power
        # else power >= 1, face-down, pop(-1), score -= 1, increase power
        
        maxScore = 0
        # i = 1
        score = 0
        while sortedTokens and (power >= sortedTokens[0] or score >= 1):
            if power >= sortedTokens[0]: # face-up
                power -= sortedTokens[0]
                score += 1
                sortedTokens.pop(0)
                # print(i,'up',power, score, sortedTokens)
            elif maxScore >= 1: # face-down
                power += sortedTokens[-1]
                score -= 1
                sortedTokens.pop()
                # print(i,'down',power, score, sortedTokens)
            else:
                return maxScore
            maxScore = max(maxScore, score)
        return maxScore