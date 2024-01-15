class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use ascii code to group possible anagrams
        # sometime ascii of 2 phrase is same but letters are diff eg. "duh" and "ill" 321
        # map = { {a:1,s:1,d:1} : ["asd", "dsa"], 
            #     {a:1,s:1} : ["as", "sa"] }
        hashmap = {}
        for s in strs:
            m = {}
            for c in s:
                m[c] = 1 + m.get(c,0)
            # print(m)
       
            m = frozenset(m.items()) # since we can't use a dict as a key for a dict, need to change to this frozenset thing
            if m not in hashmap:
                hashmap[m] = [s]
            else:
                hashmap[m].append(s)
        # print(hashmap)
        res = []
        for item in hashmap:
            res.append(hashmap[item])
        return res
