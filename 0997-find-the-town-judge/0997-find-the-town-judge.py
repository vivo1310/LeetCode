class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n < 2: return n
        # map: {person -> people trusting this person}
        hm = collections.defaultdict(list)
        
        canBeJudge = []
        for item in trust:
            hm[item[1]].append(item[0])
            if len(hm[item[1]]) == n - 1:
                canBeJudge.append(item[1])
        print(hm)
        print(canBeJudge)
        # if not hm:
        if not canBeJudge: return -1
        
        peopleWhoTrust = [x[0] for x in trust]
        i = 0
        while i < len(canBeJudge):
            print(i, canBeJudge[i], peopleWhoTrust)
            if canBeJudge[i] in peopleWhoTrust:
                return -1
            i += 1
        return canBeJudge[i-1]