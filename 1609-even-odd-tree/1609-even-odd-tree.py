# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool: 
        
#         currLevel = [root]
#         even = True
        
#         while currLevel:
#             # print(list(x.val for x in currLevel)) # traverse BFS and print level by level
#             if even:
#                 if not all(x.val % 2 == 1 for x in currLevel) \
#                     or not all(x.val < y.val for x, y in zip(currLevel, currLevel[1:])):
#                     return False
#             else:
#                 if not all(x.val % 2 == 0 for x in currLevel) \
#                     or not all(x.val > y.val for x,y in zip(currLevel, currLevel[1:])):
#                     return False
                
#             nextLevel = []
#             for node in currLevel:
#                 for child in [node.left, node.right]:
#                     if child is not None: 
#                         nextLevel.append(child)
#             currLevel = nextLevel
#             even = not even
#         return True


#         def isStrictlyOrder(lst, reverse=False):
#             stack = []
#             for i in lst:
#                 if reverse:
#                     if stack and i >= stack[-1]: return False
#                 else:
#                     if stack and i <= stack[-1]: return False
#                 stack.append(i)
#             return True

        def isStrictlyOrder(lst, reverse=False):
            if reverse:
                for i in range(len(lst) - 1):
                    if lst[i] <= lst[i+1]: return False
            else:
                for i in range(len(lst) - 1):
                    if lst[i] >= lst[i+1]: return False
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