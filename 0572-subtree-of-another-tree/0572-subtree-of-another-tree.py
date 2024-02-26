# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the starting root of subTree
        # check same tree 
        def isSameTree(p, q):
            # Null check
            if p == q == None: return True
            if not p or not q: return False
            # Equality check
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if not root: return False # traversed everything already
        
        if isSameTree(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
        
        