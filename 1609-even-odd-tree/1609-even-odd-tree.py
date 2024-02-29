# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:           
        def is_strictly_order(lst, reverse=False):
            stack = []
            for i in lst:
                if reverse:
                    if stack and i >= stack[-1]: return False
                else:
                    if stack and i <= stack[-1]: return False
                stack.append(i)
            return True
    
        def isValid(level, nodes):
            if level % 2 == 0: # even-indexed
                if not is_strictly_order(nodes): # must be strictly increasing
                    return False
                for n in nodes:
                    if n % 2 == 0: # must be odd
                        return False
                return True
            else:
                if not is_strictly_order(nodes, True): # must be strictly descreasing
                    return False
                for n in nodes:
                    if n % 2 != 0:
                        return False
                return True
            
        currLevel = [root]
        currIndex = 0

        while currLevel:
            nextLevel = []
            currLevelNodes = []
            for n in currLevel:
                # check conditions
                currLevelNodes.append(n.val)
                if n.left: 
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
           
            if not isValid(currIndex, currLevelNodes): return False

            currLevel = nextLevel
            currIndex += 1
        return True  