# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:    
        best = 0
        maxDepth = -1
        
        def dfs(node, depth):
            if not node: return
            
            nonlocal maxDepth
            nonlocal best
            if depth > maxDepth:
                maxDepth = depth
                best = node.val
                
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            # return
            
        dfs(root, 0)
        return best