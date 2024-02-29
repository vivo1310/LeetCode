# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:           
        def isStrictlyOrder(lst, reverse=False):
            stack = []
            for i in lst:
                if reverse:
                    if stack and i >= stack[-1]: return False
                else:
                    if stack and i <= stack[-1]: return False
                stack.append(i)
            return True
    
        def isValid(isEven, nodes):
            if isEven:
                if not isStrictlyOrder(nodes): # must be strictly increasing
                    return False
                for n in nodes:
                    if n % 2 == 0: # must be odd
                        return False
                return True
            else:
                if not isStrictlyOrder(nodes, reverse=True): # must be strictly descreasing
                    return False
                for n in nodes:
                    if n % 2 != 0:
                        return False
                return True
        
        # BFS, do condition check (isValid) at each level
        currLevel = [root]
        isEven = True

        while currLevel:
            nextLevel = []
            currLevelNodes = []
            for n in currLevel:
                currLevelNodes.append(n.val)
                if n.left: 
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            # check condition of Even-Odd tree
            if not isValid(isEven, currLevelNodes): return False

            currLevel = nextLevel
            isEven = not isEven # flip
        return True  