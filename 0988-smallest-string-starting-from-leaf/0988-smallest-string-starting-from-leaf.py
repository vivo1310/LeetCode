# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = 'z'*8500
        
        def dfs(node, curr):
            if not node:
                return 
            
            curr = chr(node.val + ord('a')) + curr # a - ba
    
            if not node.left and not node.right: # we're at leaf node
                nonlocal smallest
                smallest = min(smallest, curr)
                curr = curr[1:] # dba -> ba node.val = d
            dfs(node.left, curr)
            dfs(node.right, curr)
            
            
        dfs(root, '')
        return smallest